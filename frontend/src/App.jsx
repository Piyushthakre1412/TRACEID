import React, { useState, useEffect } from 'react';
import LeftPanel from './components/LeftPanel';
import KnowledgeGraph from './components/KnowledgeGraph';
import EvidenceInspector from './components/EvidenceInspector';
import { fetchIdentityGraph, searchIdentity } from './api/client';
import { Shield, Cpu, Activity, Sparkles, Database, Globe } from 'lucide-react';

export default function App() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  // Search Mode State: 'dataset' (Local DB) vs 'live' (Public Web API - Google Custom Search, GitHub, Wikipedia)
  const [searchMode, setSearchMode] = useState('dataset');

  // Filter & Weight Slider States
  const [threshold, setThreshold] = useState(70.0);
  const [weightFace, setWeightFace] = useState(0.40);
  const [weightBio, setWeightBio] = useState(0.35);
  const [weightHandle, setWeightHandle] = useState(0.25);

  const [selectedPersonId, setSelectedPersonId] = useState('P_101');
  const [selectedNode, setSelectedNode] = useState(null);

  const [searchResults, setSearchResults] = useState(null);

  useEffect(() => {
    loadGraph(selectedPersonId, threshold, weightFace, weightBio, weightHandle);
  }, [selectedPersonId, threshold, weightFace, weightBio, weightHandle]);

  const loadGraph = async (id, minThresh, wFace, wBio, wHandle) => {
    setLoading(true);
    const res = await fetchIdentityGraph(id, minThresh, wFace, wBio, wHandle);
    setData(res);
    setLoading(false);
  };

  const handleSearch = async (formData) => {
    setLoading(true);
    formData.append('mode', searchMode);
    const searchRes = await searchIdentity(formData);
    if (searchRes && searchRes.person_id && searchRes.person_id !== 'P_NOT_FOUND' && searchRes.all_matches && searchRes.all_matches.length > 0) {
      setSearchResults(searchRes.all_matches);
      const targetIds = searchRes.all_ids || searchRes.person_id;
      setSelectedPersonId(targetIds);
      await loadGraph(targetIds, threshold, weightFace, weightBio, weightHandle);
    } else {
      setSearchResults([]);
      setSelectedPersonId('P_NOT_FOUND');
      await loadGraph('P_NOT_FOUND', threshold, weightFace, weightBio, weightHandle);
    }
  };

  return (
    <div className="h-screen bg-slate-950 text-slate-100 font-sans flex flex-col overflow-hidden">
      {/* Top Header Navigation with Mode Switcher */}
      <header className="px-6 py-3 border-b border-slate-800/90 bg-slate-900/80 backdrop-blur-md flex flex-col sm:flex-row justify-between items-center gap-3 flex-shrink-0">
        <div className="flex items-center gap-3">
          <div className="p-2 rounded-xl bg-gradient-to-br from-indigo-500 to-purple-600 shadow-md shadow-indigo-500/20">
            <Cpu className="w-5 h-5 text-white" />
          </div>
          <div>
            <h1 className="text-base font-bold bg-gradient-to-r from-white via-slate-200 to-slate-400 bg-clip-text text-transparent flex items-center gap-2">
              <span>Digital Identity Intelligence Dashboard</span>
            </h1>
            <p className="text-[11px] text-slate-400">
              Multi-Modal OSINT Identity Disambiguation & React Flow Knowledge Graph • Team Ace
            </p>
          </div>
        </div>

        {/* Global Mode Switcher Toggle Pill */}
        <div className="flex items-center gap-2 bg-slate-950 p-1 rounded-xl border border-slate-800 shadow-inner">
          <button
            type="button"
            onClick={() => setSearchMode('dataset')}
            className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-bold transition-all ${
              searchMode === 'dataset'
                ? 'bg-indigo-600 text-white shadow-md shadow-indigo-600/30'
                : 'text-slate-400 hover:text-slate-200 hover:bg-slate-900'
            }`}
          >
            <Database className="w-3.5 h-3.5" />
            <span>Database Mode</span>
          </button>

          <button
            type="button"
            onClick={() => setSearchMode('live')}
            className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-bold transition-all ${
              searchMode === 'live'
                ? 'bg-gradient-to-r from-sky-500 to-blue-600 text-white shadow-md shadow-sky-500/30 ring-1 ring-sky-400/40'
                : 'text-slate-400 hover:text-slate-200 hover:bg-slate-900'
            }`}
          >
            <Globe className="w-3.5 h-3.5 text-sky-300 animate-pulse" />
            <span>Public Web Recon Mode</span>
            <span className="text-[9px] bg-sky-950 text-sky-300 border border-sky-500/40 px-1.5 py-0.5 rounded-full uppercase tracking-wider font-mono">
              Google API
            </span>
          </button>
        </div>

        <div className="hidden xl:flex items-center gap-3">
          <div className="flex items-center gap-2 bg-slate-950 border border-slate-800 px-3 py-1.5 rounded-full text-xs">
            <Activity className="w-3.5 h-3.5 text-indigo-400" />
            <span className="text-slate-300 font-mono text-[11px]">
              {searchMode === 'live' ? '🌐 Live Google OSINT API Active' : '📁 SQLite Dataset DB Active'}
            </span>
          </div>
        </div>
      </header>

      {/* Main 3-Column Dashboard Grid */}
      <main className="flex-1 p-4 md:p-6 grid grid-cols-1 lg:grid-cols-12 gap-5 overflow-hidden">
        {/* Left Column (Width: 3 cols / ~25%) */}
        <div className="lg:col-span-3 h-full overflow-hidden">
          <LeftPanel
            onSearch={handleSearch}
            searchResults={searchResults}
            allIdentities={data?.all_identities}
            threshold={threshold}
            setThreshold={setThreshold}
            weightFace={weightFace}
            setWeightFace={setWeightFace}
            weightBio={weightBio}
            setWeightBio={setWeightBio}
            weightHandle={weightHandle}
            setWeightHandle={setWeightHandle}
            selectedPersonId={selectedPersonId}
            onSelectCandidate={(id) => setSelectedPersonId(id)}
            searchMode={searchMode}
            setSearchMode={setSearchMode}
          />
        </div>

        {/* Middle Column Canvas (Width: 6 cols / ~50%) */}
        <div className="lg:col-span-6 h-full overflow-hidden relative flex flex-col">
          {loading && (
            <div className="absolute inset-0 bg-slate-950/70 backdrop-blur-sm z-30 flex flex-col items-center justify-center text-slate-300 text-xs space-y-3 rounded-2xl">
              <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-indigo-500" />
              <span>Resolving NetworkX Multi-Modal Vectors...</span>
            </div>
          )}
          <KnowledgeGraph
            graphData={data?.graph_data}
            onNodeClick={(node) => setSelectedNode(node)}
          />
        </div>

        {/* Right Column Evidence Inspector (Width: 3 cols / ~25%) */}
        <div className="lg:col-span-3 h-full overflow-hidden">
          <EvidenceInspector
            identity={data?.target_identity}
            allIdentities={data?.all_identities}
            evidenceTrail={data?.evidence_trail}
            timeline={data?.timeline}
            selectedNode={selectedNode}
          />
        </div>
      </main>
    </div>
  );
}
