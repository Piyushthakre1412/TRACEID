import React, { useState } from 'react';
import { Search, Upload, ShieldCheck, Sparkles } from 'lucide-react';

export default function SearchSection({ onSearch }) {
  const [query, setQuery] = useState('');
  const [file, setFile] = useState(null);

  const handleSubmit = (e) => {
    e.preventDefault();
    const formData = new FormData();
    if (query) formData.append('query', query);
    if (file) formData.append('file', file);
    onSearch(formData);
  };

  return (
    <div className="bg-slate-900 border border-slate-800 rounded-xl p-6 shadow-2xl mb-8">
      <div className="flex items-center justify-between mb-4">
        <div>
          <h2 className="text-xl font-bold text-white flex items-center gap-2">
            <Sparkles className="w-5 h-5 text-indigo-400" />
            Identity Search & Seed Ingestion
          </h2>
          <p className="text-xs text-slate-400">
            Upload candidate portrait image or enter social handle / canonical name for multi-modal resolution.
          </p>
        </div>
        <div className="flex items-center gap-2 bg-indigo-950/60 border border-indigo-500/30 text-indigo-300 text-xs px-3 py-1.5 rounded-full">
          <ShieldCheck className="w-4 h-4 text-indigo-400" />
          <span>Multi-Modal Scoring Active</span>
        </div>
      </div>

      <form onSubmit={handleSubmit} className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div className="md:col-span-2 relative">
          <Search className="absolute left-3 top-3.5 w-4 h-4 text-slate-400" />
          <input
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="Search handle (e.g. @piyush-thakre) or canonical name..."
            className="w-full bg-slate-950 border border-slate-800 rounded-lg pl-10 pr-4 py-3 text-sm text-white placeholder-slate-500 focus:outline-none focus:border-indigo-500 transition-colors"
          />
        </div>

        <div className="flex gap-2">
          <label className="flex-1 bg-slate-950 border border-slate-800 hover:border-slate-700 rounded-lg px-3 py-2 flex items-center justify-center gap-2 cursor-pointer transition-colors text-xs text-slate-300">
            <Upload className="w-4 h-4 text-slate-400" />
            <span className="truncate">{file ? file.name : "Upload Image"}</span>
            <input
              type="file"
              accept="image/*"
              className="hidden"
              onChange={(e) => setFile(e.target.files[0])}
            />
          </label>

          <button
            type="submit"
            className="bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-semibold px-5 py-3 rounded-lg transition-colors flex items-center gap-2 shadow-lg shadow-indigo-600/20"
          >
            <span>Resolve Identity</span>
          </button>
        </div>
      </form>
    </div>
  );
}
