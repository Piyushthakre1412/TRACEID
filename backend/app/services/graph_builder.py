import networkx as nx
import math

class GraphBuilder:
    def __init__(self):
        self.G = nx.Graph()

    def build_from_dataset(self, nodes_data: list, edges_data: list):
        """Constructs NetworkX graph from nodes and edges dataset."""
        self.G.clear()
        for node in nodes_data:
            self.G.add_node(
                node["id"],
                label=node["label"],
                type=node["type"],
                image=node.get("image", ""),
                metadata=node.get("metadata", {})
            )
        for edge in edges_data:
            self.G.add_edge(
                edge["source"],
                edge["target"],
                relationship=edge.get("relationship", "CONNECTED"),
                confidence=float(edge.get("confidence", 90.0))
            )

    def build_from_candidates(self, candidates: list):
        """Constructs graph automatically from candidate objects."""
        self.G.clear()
        for candidate in candidates:
            p_id = candidate["person_id"]
            self.G.add_node(p_id, label=candidate["canonical_name"], type="person", image=candidate.get("primary_image", ""))
            
            # Add handle nodes
            for idx, handle in enumerate(candidate.get("handles", [])):
                h_id = f"H_{p_id}_{idx}"
                self.G.add_node(h_id, label=f"@{handle['username']} ({handle['platform']})", type="handle", url=handle.get("url", ""))
                self.G.add_edge(p_id, h_id, relationship="OWNED_BY", confidence=92.0)
            
            # Add organization node
            if candidate.get("institution"):
                org_id = f"ORG_{p_id}"
                self.G.add_node(org_id, label=candidate["institution"], type="organization")
                self.G.add_edge(p_id, org_id, relationship="AFFILIATED_WITH", confidence=95.0)

            # Add project nodes
            for idx, proj in enumerate(candidate.get("projects", [])):
                proj_id = f"PROJ_{p_id}_{idx}"
                self.G.add_node(proj_id, label=proj, type="project")
                self.G.add_edge(p_id, proj_id, relationship="CONTRIBUTED_TO", confidence=88.0)

    def get_react_flow_graph(self, target_person_id: str = "P_101", min_threshold: float = 70.0, max_nodes: int = 30) -> dict:
        """
        Calculates spacious, non-overlapping orbital layout coordinates around target persons
        and returns JSON formatted specifically for React Flow (<ReactFlow />).
        """
        if not self.G.nodes or target_person_id == "P_NOT_FOUND":
            return {"nodes": [], "edges": []}

        target_ids = [p.strip() for p in target_person_id.split(",") if p.strip()]
        valid_targets = [t for t in target_ids if t in self.G]

        if not valid_targets:
            # Fallback: find first 1-2 person nodes in G
            person_nodes = [n for n, d in self.G.nodes(data=True) if d.get("type") == "person"]
            if person_nodes:
                valid_targets = person_nodes[:2]
            else:
                valid_targets = list(self.G.nodes)[:1]

        all_target_nodes = set()
        for t in valid_targets:
            if t in self.G:
                all_target_nodes.add(t)
                neighbors = [
                    n for n in self.G.neighbors(t)
                    if self.G.edges[t, n].get("confidence", 100.0) >= min_threshold
                ]
                all_target_nodes.update(neighbors)

        sub_graph = self.G.subgraph(list(all_target_nodes)).copy()

        if len(sub_graph.nodes) == 0:
            return {"nodes": [], "edges": []}

        # Cap total node count to max_nodes to prevent canvas clutter
        if len(sub_graph.nodes) > max_nodes:
            priority_nodes = list(valid_targets)
            for t in valid_targets:
                if t in sub_graph:
                    priority_nodes.extend(list(sub_graph.neighbors(t)))
            priority_nodes = list(dict.fromkeys(priority_nodes))[:max_nodes]
            sub_graph = sub_graph.subgraph(priority_nodes).copy()

        pos = {}
        target_list = [t for t in valid_targets if t in sub_graph]
        if not target_list:
            target_list = list(sub_graph.nodes)[:1]

        # Spacious multi-center orbital positioning layout
        for t_idx, t_id in enumerate(target_list):
            center_x = 320 + (t_idx * 520)
            center_y = 280
            pos[t_id] = (center_x, center_y)
            
            t_neighbors = [n for n in sub_graph.neighbors(t_id) if n not in target_list]
            
            # Group neighbors by category
            handle_nodes = [n for n in t_neighbors if sub_graph.nodes[n].get("type") == "handle"]
            org_nodes = [n for n in t_neighbors if sub_graph.nodes[n].get("type") == "organization"]
            proj_nodes = [n for n in t_neighbors if sub_graph.nodes[n].get("type") == "project"]
            other_nodes = [n for n in t_neighbors if n not in handle_nodes and n not in org_nodes and n not in proj_nodes]

            # Ring 1: Handles (Radius = 210px)
            num_h = len(handle_nodes)
            for idx, n_id in enumerate(handle_nodes):
                angle = (2 * math.pi * idx) / max(1, num_h) - (math.pi / 4)
                pos[n_id] = (center_x + 220 * math.cos(angle), center_y + 160 * math.sin(angle))

            # Ring 2: Projects (Radius = 310px)
            num_p = len(proj_nodes)
            for idx, n_id in enumerate(proj_nodes):
                angle = (2 * math.pi * idx) / max(1, num_p) + (math.pi / 3)
                pos[n_id] = (center_x + 310 * math.cos(angle), center_y + 220 * math.sin(angle))

            # Ring 3: Organizations (Top/Bottom offset)
            for idx, n_id in enumerate(org_nodes):
                y_offset = -230 if idx % 2 == 0 else 230
                pos[n_id] = (center_x + (idx * 220 - 110), center_y + y_offset)

            # Ring 4: Other nodes
            num_ot = len(other_nodes)
            for idx, n_id in enumerate(other_nodes):
                angle = (2 * math.pi * idx) / max(1, num_ot)
                pos[n_id] = (center_x + 360 * math.cos(angle), center_y + 260 * math.sin(angle))

        # Position any remaining orphan nodes cleanly
        for idx, n_id in enumerate(sub_graph.nodes()):
            if n_id not in pos:
                pos[n_id] = (150 + (idx * 180), 480)

        react_nodes = []
        for n_id, data in sub_graph.nodes(data=True):
            coords = pos.get(n_id, (320, 280))
            if not isinstance(coords, tuple):
                coords = (coords[0], coords[1])
            node_type = data.get("type", "person")
            react_nodes.append({
                "id": n_id,
                "type": node_type,
                "position": {"x": round(coords[0], 1), "y": round(coords[1], 1)},
                "data": {
                    "label": data.get("label", n_id),
                    "type": node_type,
                    "image": data.get("image", ""),
                    "canonical_name": data.get("label", n_id),
                    "url": data.get("url", "")
                }
            })

        react_edges = []
        for idx, (u, v, data) in enumerate(sub_graph.edges(data=True)):
            confidence = data.get("confidence", 90.0)
            relationship = data.get("relationship", "CONNECTED")
            edge_id = f"e_{u}_{v}_{idx}"

            stroke_color = "#10b981" if confidence >= 85.0 else "#6366f1"

            react_edges.append({
                "id": edge_id,
                "source": u,
                "target": v,
                "label": f"{relationship} ({confidence}%)",
                "type": "smoothstep",
                "animated": confidence >= 85.0,
                "style": {
                    "stroke": stroke_color,
                    "strokeWidth": 2
                },
                "data": {
                    "relationship": relationship,
                    "confidence": confidence
                }
            })

        return {"nodes": react_nodes, "edges": react_edges}

graph_builder = GraphBuilder()

