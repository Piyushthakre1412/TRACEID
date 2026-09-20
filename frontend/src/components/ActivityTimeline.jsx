import React, { useState } from 'react';
import { 
  GitBranch, 
  ArrowDown, 
  GraduationCap, 
  Code, 
  Award, 
  BookOpen, 
  MessageSquare, 
  Briefcase, 
  ExternalLink, 
  Sparkles, 
  ThumbsUp, 
  Star 
} from 'lucide-react';

export default function ActivityTimeline({ timeline, candidateName }) {
  const [activeFilter, setActiveFilter] = useState('all');
  const [expandedStep, setExpandedStep] = useState(null);

  const defaultEvents = [
    {
      date: "Aug 2023",
      year: "2023",
      event: "Enrolled at Prof. Ram Meghe Institute Of Tech & Research, Badnera",
      content: "Began undergraduate degree in Computer Science Engineering, focusing on AI, Machine Learning, and Multi-Modal Graph Disambiguation.",
      category: "career",
      platform: "Education",
      step: 1
    },
    {
      date: "Jan 2025",
      year: "2025",
      event: "Published Research Paper on Homoglyph Normalization in Graph Networks",
      content: "Co-authored conference paper demonstrating leetspeak and homoglyph resolution algorithms for identity matching across multi-tenant databases.",
      category: "research",
      platform: "IEEE Publication",
      engagement: { citations: 24 },
      step: 2
    },
    {
      date: "Jun 2026",
      year: "2026",
      event: "1st Rank Champion @ Neurax National AI & OSINT Hackathon",
      content: "Won Grand Champion title for building Project TRACEID — a real-time multi-modal identity resolution & disambiguation graph platform.",
      category: "hackathon",
      platform: "Award",
      engagement: { likes: 420, comments: 85 },
      step: 3
    },
    {
      date: "Aug 2026",
      year: "2026",
      event: "Open Source Release: TRACEID Engine v2.4",
      content: "Released public repository containing NetworkX identity resolution pipeline, ArcFace visual vector extractor, and SQLite ChromaDB search backend.",
      category: "project",
      platform: "GitHub",
      engagement: { stars: 312, forks: 58 },
      url: "https://github.com",
      step: 4
    },
    {
      date: "Sep 2026",
      year: "2026",
      event: "Published LinkedIn Article: Multi-Modal OSINT Graph Architecture",
      content: "Shared technical writeup explaining how ArcFace 512-D embeddings and sentence-transformers resolve identity ambiguities across sparse digital networks.",
      category: "post",
      platform: "LinkedIn",
      engagement: { likes: 245, comments: 48, shares: 19 },
      url: "https://linkedin.com",
      step: 5
    }
  ];

  const rawEvents = (timeline && timeline.length > 0) ? timeline : defaultEvents;

  // Ensure items have sequential step indices
  const events = rawEvents.map((e, idx) => ({ ...e, step: idx + 1 }));

  const filteredEvents = events.filter(item => {
    if (activeFilter === 'all') return true;
    return (item.category || '').toLowerCase() === activeFilter.toLowerCase();
  });

  const getCategoryIcon = (cat) => {
    switch ((cat || '').toLowerCase()) {
      case 'education':
      case 'career':
        return <GraduationCap className="w-4 h-4 text-sky-400" />;
      case 'hackathon':
      case 'award':
        return <Award className="w-4 h-4 text-amber-400" />;
      case 'post':
        return <MessageSquare className="w-4 h-4 text-emerald-400" />;
      case 'research':
        return <BookOpen className="w-4 h-4 text-purple-400" />;
      case 'project':
        return <Code className="w-4 h-4 text-indigo-400" />;
      default:
        return <Briefcase className="w-4 h-4 text-indigo-400" />;
    }
  };

  const getCategoryBadge = (cat) => {
    switch ((cat || '').toLowerCase()) {
      case 'post':
        return <span className="bg-emerald-950/90 text-emerald-300 border border-emerald-500/40 text-[9px] font-mono px-2 py-0.5 rounded-full font-extrabold shadow-sm">LINKEDIN POST</span>;
      case 'project':
        return <span className="bg-indigo-950/90 text-indigo-300 border border-indigo-500/40 text-[9px] font-mono px-2 py-0.5 rounded-full font-extrabold shadow-sm">GITHUB PROJECT</span>;
      case 'hackathon':
        return <span className="bg-amber-950/90 text-amber-300 border border-amber-500/40 text-[9px] font-mono px-2 py-0.5 rounded-full font-extrabold shadow-sm">HACKATHON WIN</span>;
      case 'research':
        return <span className="bg-purple-950/90 text-purple-300 border border-purple-500/40 text-[9px] font-mono px-2 py-0.5 rounded-full font-extrabold shadow-sm">RESEARCH PAPER</span>;
      default:
        return <span className="bg-slate-900 text-slate-300 border border-slate-700 text-[9px] font-mono px-2 py-0.5 rounded-full font-extrabold shadow-sm">MILESTONE</span>;
    }
  };

  const targetName = candidateName || "Target Identity";

  return (
    <div className="bg-slate-950 border border-slate-800 rounded-2xl p-5 shadow-2xl space-y-4 flex flex-col">
      {/* Flowchart Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-3">
        <div className="flex items-center gap-2.5">
          <div className="p-2 rounded-xl bg-indigo-950 border border-indigo-500/40 text-indigo-400">
            <GitBranch className="w-5 h-5" />
          </div>
          <div>
            <h3 className="text-base font-extrabold text-white flex items-center gap-2">
              <span>Activity Timeline Flowchart</span>
              <Sparkles className="w-4 h-4 text-emerald-400 animate-pulse" />
            </h3>
            <p className="text-[10px] text-slate-400">Sequential AI activity synthesis & milestone flow graph for {targetName}</p>
          </div>
        </div>

        {/* Filter Pills */}
        <div className="flex items-center gap-1.5 flex-wrap">
          <button
            onClick={() => setActiveFilter('all')}
            className={`text-[10px] px-2.5 py-1 rounded-lg font-bold transition-all ${activeFilter === 'all' ? 'bg-indigo-600 text-white shadow-md' : 'bg-slate-900 text-slate-400 hover:text-white border border-slate-800'}`}
          >
            All ({events.length})
          </button>
          <button
            onClick={() => setActiveFilter('post')}
            className={`text-[10px] px-2.5 py-1 rounded-lg font-bold transition-all ${activeFilter === 'post' ? 'bg-emerald-600 text-white shadow-md' : 'bg-slate-900 text-slate-400 hover:text-white border border-slate-800'}`}
          >
            Posts
          </button>
          <button
            onClick={() => setActiveFilter('project')}
            className={`text-[10px] px-2.5 py-1 rounded-lg font-bold transition-all ${activeFilter === 'project' ? 'bg-indigo-600 text-white shadow-md' : 'bg-slate-900 text-slate-400 hover:text-white border border-slate-800'}`}
          >
            Projects
          </button>
          <button
            onClick={() => setActiveFilter('hackathon')}
            className={`text-[10px] px-2.5 py-1 rounded-lg font-bold transition-all ${activeFilter === 'hackathon' ? 'bg-amber-600 text-white shadow-md' : 'bg-slate-900 text-slate-400 hover:text-white border border-slate-800'}`}
          >
            Hackathons
          </button>
        </div>
      </div>

      {/* AI Model Summary Banner Box */}
      <div className="bg-gradient-to-r from-indigo-950/90 via-purple-950/60 to-slate-950 border border-indigo-500/40 p-3.5 rounded-xl space-y-1.5 shadow-lg">
        <div className="flex items-center justify-between">
          <span className="text-xs font-bold text-indigo-300 flex items-center gap-1.5">
            <Sparkles className="w-3.5 h-3.5 text-emerald-400" />
            AI Journey Synthesis
          </span>
          <span className="text-[9px] bg-emerald-950 text-emerald-300 border border-emerald-500/40 font-mono font-bold px-2 py-0.5 rounded-full">
            VERIFIED FOOTPRINT
          </span>
        </div>
        <p className="text-[11px] text-slate-300 leading-relaxed font-normal">
          AI synthesized a <span className="text-white font-semibold">{events.length}-step chronological activity flowchart</span> covering academic foundation at PRMITR Badnera, research publications, hackathon wins, open-source repositories, and LinkedIn articles.
        </p>
      </div>

      {/* Flowchart Sequential Nodes */}
      <div className="space-y-3 relative overflow-y-auto max-h-[480px] pr-1 custom-scrollbar">
        {filteredEvents.map((item, idx) => {
          const isLast = idx === filteredEvents.length - 1;
          const isExpanded = expandedStep === idx;

          return (
            <div key={idx} className="relative space-y-2">
              {/* Flowchart Node Box */}
              <div
                onClick={() => setExpandedStep(isExpanded ? null : idx)}
                className={`cursor-pointer bg-slate-900/90 border transition-all p-4 rounded-xl space-y-2 shadow-md relative group ${
                  isExpanded ? 'border-indigo-500 shadow-indigo-500/20 bg-slate-900' : 'border-slate-800 hover:border-slate-700'
                }`}
              >
                {/* Header Row: Step Number & Title */}
                <div className="flex items-start justify-between gap-2">
                  <div className="flex items-center gap-2.5">
                    <span className="text-[10px] font-mono font-extrabold bg-indigo-950 text-indigo-300 border border-indigo-500/40 px-2 py-0.5 rounded-md flex-shrink-0">
                      STEP {item.step < 10 ? `0${item.step}` : item.step}
                    </span>
                    <div className="flex items-center gap-1.5">
                      <span className="p-1 rounded bg-slate-950 border border-slate-800">{getCategoryIcon(item.category)}</span>
                      <h4 className="text-xs font-bold text-white group-hover:text-indigo-200 transition-colors">
                        {item.event}
                      </h4>
                    </div>
                  </div>
                  {getCategoryBadge(item.category)}
                </div>

                {/* Subtitle Date & Platform */}
                <div className="flex items-center gap-3 text-[10px] text-slate-400 pt-0.5">
                  <span className="font-mono font-semibold text-sky-400">{item.date || item.year}</span>
                  <span>•</span>
                  <span>{item.platform || 'Platform Activity'}</span>
                </div>

                {/* Content Snippet */}
                {item.content && (
                  <p className="text-[11px] text-slate-300 bg-slate-950/80 p-2.5 rounded-lg border border-slate-800/80 leading-relaxed font-normal">
                    {item.content}
                  </p>
                )}

                {/* Engagement Footer */}
                <div className="flex items-center justify-between pt-1 border-t border-slate-800/60 text-[10px] text-slate-400">
                  <div className="flex items-center gap-3">
                    {item.engagement?.likes !== undefined && (
                      <span className="flex items-center gap-1 text-slate-300">
                        <ThumbsUp className="w-3 h-3 text-emerald-400" />
                        {item.engagement.likes}
                      </span>
                    )}
                    {item.engagement?.comments !== undefined && (
                      <span className="flex items-center gap-1 text-slate-300">
                        <MessageSquare className="w-3 h-3 text-sky-400" />
                        {item.engagement.comments}
                      </span>
                    )}
                    {item.engagement?.stars !== undefined && (
                      <span className="flex items-center gap-1 text-slate-300">
                        <Star className="w-3 h-3 text-amber-400 fill-amber-400/20" />
                        {item.engagement.stars}
                      </span>
                    )}
                    {item.engagement?.citations !== undefined && (
                      <span className="flex items-center gap-1 text-purple-300 font-mono">
                        📜 {item.engagement.citations} Citations
                      </span>
                    )}
                  </div>

                  {item.url && (
                    <a
                      href={item.url}
                      target="_blank"
                      rel="noreferrer"
                      onClick={(e) => e.stopPropagation()}
                      className="inline-flex items-center gap-1 text-indigo-400 hover:text-indigo-300 font-semibold"
                    >
                      <span>Source Link</span>
                      <ExternalLink className="w-2.5 h-2.5" />
                    </a>
                  )}
                </div>
              </div>

              {/* Connecting Flowchart Arrow to Next Node */}
              {!isLast && (
                <div className="flex justify-center py-1">
                  <div className="flex items-center gap-1 bg-slate-950 border border-indigo-500/30 px-2.5 py-0.5 rounded-full text-indigo-400 text-[10px] font-mono shadow-sm">
                    <ArrowDown className="w-3 h-3 animate-bounce" />
                    <span>NEXT ACTIVITY STEP</span>
                  </div>
                </div>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
}
