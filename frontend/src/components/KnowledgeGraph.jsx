import React, { useEffect, useMemo } from 'react';
import {
  ReactFlow,
  Controls,
  Background,
  MiniMap,
  useNodesState,
  useEdgesState,
  Handle,
  Position
} from '@xyflow/react';
import '@xyflow/react/dist/style.css';
import { User, Cpu, Building, FolderGit2, Network, ExternalLink, UserX } from 'lucide-react';

// Custom Node: Person Node
const PersonNode = ({ data }) => (
  <div className="bg-slate-900/95 border-2 border-indigo-500 rounded-2xl p-3.5 shadow-xl shadow-indigo-500/20 min-w-[170px] text-center backdrop-blur-md">
    <Handle type="target" position={Position.Top} className="!bg-indigo-500 !w-2.5 !h-2.5" />
    <div className="flex items-center justify-center gap-2 mb-1.5">
      <div className="p-2 rounded-xl bg-indigo-950/80 border border-indigo-500/40 text-indigo-300">
        <User className="w-4 h-4" />
      </div>
      <span className="text-[10px] uppercase font-bold text-indigo-400 tracking-wider">Canonical</span>
    </div>
    <div className="text-xs font-bold text-white tracking-wide">{data.label || data.canonical_name}</div>
    <div className="text-[10px] text-slate-400 mt-0.5">{data.type || 'Person Entity'}</div>
    <Handle type="source" position={Position.Bottom} className="!bg-indigo-500 !w-2.5 !h-2.5" />
  </div>
);

// Custom Node: Handle Node
const HandleNode = ({ data }) => (
  <div className="bg-slate-950/90 border border-emerald-500/60 rounded-xl p-3 shadow-lg shadow-emerald-500/10 min-w-[150px] text-center backdrop-blur-md">
    <Handle type="target" position={Position.Top} className="!bg-emerald-400 !w-2 !h-2" />
    <div className="flex items-center justify-center gap-1.5 mb-1">
      <Cpu className="w-3.5 h-3.5 text-emerald-400" />
      <span className="text-[9px] uppercase font-semibold text-emerald-400">Handle</span>
    </div>
    <div className="text-xs font-semibold text-slate-200 truncate">{data.label}</div>
    <Handle type="source" position={Position.Bottom} className="!bg-emerald-400 !w-2 !h-2" />
  </div>
);

// Custom Node: Organization Node
const OrgNode = ({ data }) => (
  <div className="bg-slate-950/90 border border-amber-500/60 rounded-xl p-3 shadow-lg shadow-amber-500/10 min-w-[150px] text-center backdrop-blur-md">
    <Handle type="target" position={Position.Top} className="!bg-amber-400 !w-2 !h-2" />
    <div className="flex items-center justify-center gap-1.5 mb-1">
      <Building className="w-3.5 h-3.5 text-amber-400" />
      <span className="text-[9px] uppercase font-semibold text-amber-400">Organization</span>
    </div>
    <div className="text-xs font-semibold text-slate-200 truncate">{data.label}</div>
    <Handle type="source" position={Position.Bottom} className="!bg-amber-400 !w-2 !h-2" />
  </div>
);

// Custom Node: Project Node
const ProjectNode = ({ data }) => (
  <div className="bg-slate-950/90 border border-sky-500/60 rounded-xl p-3 shadow-lg shadow-sky-500/10 min-w-[150px] text-center backdrop-blur-md">
    <Handle type="target" position={Position.Top} className="!bg-sky-400 !w-2 !h-2" />
    <div className="flex items-center justify-center gap-1.5 mb-1">
      <FolderGit2 className="w-3.5 h-3.5 text-sky-400" />
      <span className="text-[9px] uppercase font-semibold text-sky-400">Project</span>
    </div>
    <div className="text-xs font-semibold text-slate-200 truncate">{data.label}</div>
    <Handle type="source" position={Position.Bottom} className="!bg-sky-400 !w-2 !h-2" />
  </div>
);

export default function KnowledgeGraph({ graphData, onNodeClick }) {
  const nodeTypes = useMemo(() => ({
    person: PersonNode,
    handle: HandleNode,
    organization: OrgNode,
    project: ProjectNode
  }), []);

  const [nodes, setNodes, onNodesChange] = useNodesState([]);
  const [edges, setEdges, onEdgesChange] = useEdgesState([]);

  useEffect(() => {
    if (graphData && graphData.nodes) {
      setNodes(graphData.nodes);
      setEdges(graphData.edges || []);
    }
  }, [graphData, setNodes, setEdges]);

  return (
    <div className="bg-slate-900 border border-slate-800 rounded-2xl p-5 shadow-2xl h-full flex flex-col justify-between relative overflow-hidden">
      {/* Canvas Top Bar */}
      <div className="flex items-center justify-between mb-3 z-10">
        <div className="flex items-center gap-2">
          <div className="p-2 rounded-xl bg-slate-950 border border-slate-800">
            <Network className="w-4 h-4 text-emerald-400" />
          </div>
          <div>
            <h3 className="text-base font-bold text-white">Multi-Modal Knowledge Graph Canvas</h3>
            <p className="text-[11px] text-slate-400">Interactive NetworkX Graph & React Flow Engine</p>
          </div>
        </div>

        <div className="flex items-center gap-2">
          <span className="text-xs bg-emerald-950/80 border border-emerald-500/30 text-emerald-400 px-3 py-1 rounded-full font-semibold">
            {nodes.length} Active Nodes
          </span>
        </div>
      </div>

      {/* Main ReactFlow Workspace */}
      <div className="flex-1 w-full min-h-[480px] bg-slate-950 border border-slate-800/80 rounded-xl relative overflow-hidden">
        {(!nodes || nodes.length === 0) && (
          <div className="absolute inset-0 z-20 flex flex-col items-center justify-center bg-slate-950/95 text-center p-6 space-y-3 rounded-xl backdrop-blur-md">
            <div className="p-3 bg-rose-950/80 border border-rose-500/40 rounded-2xl text-rose-400 shadow-lg">
              <UserX className="w-8 h-8" />
            </div>
            <h3 className="text-sm font-bold text-white">Target User Does Not Exist in Database</h3>
            <p className="text-xs text-slate-400 max-w-sm leading-relaxed">
              No identity profile or graph nodes available. Try searching for an indexed target (e.g. Aarav Sharma, Satwik Mhasaye, John Smith, Piyush Thakre).
            </p>
          </div>
        )}
        <ReactFlow
          nodes={nodes}
          edges={edges}
          onNodesChange={onNodesChange}
          onEdgesChange={onEdgesChange}
          onNodeClick={(_, node) => onNodeClick && onNodeClick(node)}
          nodeTypes={nodeTypes}
          fitView
          fitViewOptions={{ padding: 0.2 }}
          defaultEdgeOptions={{ type: 'smoothstep', animated: true }}
          className="bg-slate-950"
        >
          <Background color="#334155" gap={24} size={1} />
          <Controls className="!bg-slate-900 !border-slate-800 !text-slate-200 rounded-lg overflow-hidden shadow-xl" />
          <MiniMap
            nodeColor={(node) => {
              switch (node.type) {
                case 'person': return '#6366f1';
                case 'handle': return '#10b981';
                case 'organization': return '#f59e0b';
                case 'project': return '#0ea5e9';
                default: return '#64748b';
              }
            }}
            maskColor="rgba(15, 23, 42, 0.7)"
            className="!bg-slate-900/90 !border-slate-800 rounded-lg"
          />
        </ReactFlow>
      </div>

      {/* Canvas Footer Legend */}
      <div className="mt-3 flex flex-wrap gap-4 text-xs text-slate-400 justify-center border-t border-slate-800/60 pt-3">
        <div className="flex items-center gap-1.5">
          <span className="w-2.5 h-2.5 rounded-full bg-indigo-500" />
          <span>Person Entity</span>
        </div>
        <div className="flex items-center gap-1.5">
          <span className="w-2.5 h-2.5 rounded-full bg-emerald-400" />
          <span>Handle Alias</span>
        </div>
        <div className="flex items-center gap-1.5">
          <span className="w-2.5 h-2.5 rounded-full bg-amber-400" />
          <span>Organization</span>
        </div>
        <div className="flex items-center gap-1.5">
          <span className="w-2.5 h-2.5 rounded-full bg-sky-400" />
          <span>Project Repo</span>
        </div>
      </div>
    </div>
  );
}
