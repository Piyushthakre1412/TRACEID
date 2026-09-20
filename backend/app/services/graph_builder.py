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

    def get_react_flow_graph(self, target_person_id: str = "P_101", min_threshold: float = 70.0) -> dict:
        """
        Calculates layout coordinates using NetworkX radial positioning around target persons
        and returns JSON formatted specifically for React Flow (<ReactFlow />).
        """
        if not self.G.nodes:
            return {"nodes": [], "edges": []}

        target_ids = [p.strip() for p in target_person_id.split(",") if p.strip()]
        valid_targets = [t for t in target_ids if t in self.G]

        if valid_targets:
            all_target_nodes = set()
            for t in valid_targets:
                all_target_nodes.add(t)
                neighbors = [n for n in self.G.neighbors(t) if self.G.edges[t, n].get("confidence", 100.0) >= min_threshold]
                all_target_nodes.update(neighbors)
            sub_graph = self.G.subgraph(list(all_target_nodes)).copy()
        else:
            filtered_edges = [
                (u, v, data) for u, v, data in self.G.edges(data=True)
                if data.get("confidence", 100.0) >= min_threshold
            ]
            sub_graph = nx.Graph()
            for u, v, data in filtered_edges:
                sub_graph.add_node(u, **self.G.nodes[u])
                sub_graph.add_node(v, **self.G.nodes[v])
                sub_graph.add_edge(u, v, **data)

        if len(sub_graph.nodes) == 0:
            sub_graph = self.G

        pos = {}
        if valid_targets:
            for t_idx, t_id in enumerate(valid_targets):
                center_x = 260 + (t_idx * 380)
                center_y = 250
                pos[t_id] = (center_x, center_y)
                
                t_neighbors = [n for n in sub_graph.neighbors(t_id) if n not in valid_targets]
                num_neigh = len(t_neighbors)
                for idx, n_id in enumerate(t_neighbors):
                    angle = (2 * math.pi * idx) / max(1, num_neigh)
                    pos[n_id] = (center_x + 160 * math.cos(angle), center_y + 140 * math.sin(angle))
        else:
            pos = nx.spring_layout(sub_graph, k=2.5, iterations=50, seed=42)

        react_nodes = []
        for n_id, data in sub_graph.nodes(data=True):
            coords = pos.get(n_id, (400, 250))
            if not isinstance(coords, tuple):
                coords = (coords[0] * 320 + 400, coords[1] * 240 + 250)
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

            # Dynamic styling based on confidence
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
