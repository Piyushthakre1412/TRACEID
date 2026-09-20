import React, { useState } from 'react';
import { Calendar, Award, GraduationCap, Code, MessageSquare, ThumbsUp, Star, ExternalLink, Share2, BookOpen, Briefcase, Filter } from 'lucide-react';

export default function ActivityTimeline({ timeline }) {
  const [activeFilter, setActiveFilter] = useState('all');

  const defaultEvents = [
    {
      date: "Sep 2026",
      year: "2026",
      event: "Published LinkedIn Article: Multi-Modal OSINT Graph Disambiguation Architecture",
      content: "Excited to share our technical writeup on combining ArcFace visual embeddings with sentence-transformers for entity resolution across sparse digital identity networks.",
      category: "post",
      platform: "LinkedIn",
      engagement: { likes: 184, comments: 32, shares: 14 },
      url: "https://linkedin.com"
    },
    {
      date: "Aug 2026",
      year: "2026",
      event: "Open Source Release: TRACEID / InterceptAI Engine v2.4",
      content: "Pushed release v2.4 containing NetworkX identity resolution pipeline and SQLite ChromaDB vector search backend.",
      category: "project",
      platform: "GitHub",
      engagement: { stars: 240, forks: 45 },
      url: "https://github.com"
    },
    {
      date: "Jun 2026",
      year: "2026",
      event: "Grand Winner @ National AI & OSINT Hackathon 2026",
      content: "Proud to announce our team won 1st Place for building real-time multi-modal identity resolution systems.",
      category: "hackathon",
      platform: "Award",
      engagement: { likes: 310, comments: 58 }
    },
    {
      date: "Jul 2025",
      year: "2025",
      event: "Published IEEE Conference Paper on Vector Space Disambiguation",
      content: "Paper titled 'A Robust Hybrid Similarity Benchmark for Homoglyph and Leetspeak Identity Resolution' accepted at IEEE AI 2025.",
      category: "research",
      platform: "Publication",
      engagement: { citations: 19 }
    },
    {
      date: "Aug 2023",
      year: "2023",
      event: "Enrolled at Prof. Ram Meghe Institute Of Tech & Research, Badnera",
      content: "Started Bachelor of Technology degree specializing in Computer Science, Artificial Intelligence and Machine Learning.",
      category: "career",
      platform: "Education"
    }
  ];

  const events = (timeline && timeline.length > 0) ? timeline : defaultEvents;

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
        return <span className="bg-emerald-950/80 text-emerald-300 border border-emerald-800/60 text-[9px] font-mono px-2 py-0.5 rounded-full font-bold">LINKEDIN POST</span>;
      case 'project':
        return <span className="bg-indigo-950/80 text-indigo-300 border border-indigo-800/60 text-[9px] font-mono px-2 py-0.5 rounded-full font-bold">GITHUB PROJECT</span>;
      case 'hackathon':
        return <span className="bg-amber-950/80 text-amber-300 border border-amber-800/60 text-[9px] font-mono px-2 py-0.5 rounded-full font-bold">HACKATHON WIN</span>;
      case 'research':
        return <span className="bg-purple-950/80 text-purple-300 border border-purple-800/60 text-[9px] font-mono px-2 py-0.5 rounded-full font-bold">RESEARCH PAPER</span>;
      default:
        return <span className="bg-slate-900 text-slate-300 border border-slate-700 text-[9px] font-mono px-2 py-0.5 rounded-full font-bold">MILESTONE</span>;
    }
  };

  const counts = {
    all: events.length,
    post: events.filter(e => (e.category || '').toLowerCase() === 'post').length,
    project: events.filter(e => (e.category || '').toLowerCase() === 'project').length,
    hackathon: events.filter(e => (e.category || '').toLowerCase() === 'hackathon').length,
    research: events.filter(e => (e.category || '').toLowerCase() === 'research').length
  };

  return (
    <div className="bg-slate-950 border border-slate-800 rounded-xl p-5 shadow-2xl h-full flex flex-col space-y-4">
      {/* Header & Filter Controls */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800/80 pb-3">
        <div className="flex items-center gap-2">
          <Calendar className="w-5 h-5 text-indigo-400" />
          <div>
            <h3 className="text-base font-extrabold text-white">User Activity & Post Graph</h3>
            <p className="text-[10px] text-slate-400">Tracked posts, open source releases, research papers & awards</p>
          </div>
        </div>

        {/* Filter Pills */}
        <div className="flex flex-wrap items-center gap-1.5">
          <button
            onClick={() => setActiveFilter('all')}
            className={`text-[10px] px-2.5 py-1 rounded-md font-semibold transition-all ${activeFilter === 'all' ? 'bg-indigo-600 text-white shadow-md' : 'bg-slate-900 text-slate-400 hover:text-white border border-slate-800'}`}
          >
            All ({counts.all})
          </button>
          <button
            onClick={() => setActiveFilter('post')}
            className={`text-[10px] px-2.5 py-1 rounded-md font-semibold transition-all ${activeFilter === 'post' ? 'bg-emerald-600 text-white shadow-md' : 'bg-slate-900 text-slate-400 hover:text-white border border-slate-800'}`}
          >
            Posts ({counts.post})
          </button>
          <button
            onClick={() => setActiveFilter('project')}
            className={`text-[10px] px-2.5 py-1 rounded-md font-semibold transition-all ${activeFilter === 'project' ? 'bg-indigo-600 text-white shadow-md' : 'bg-slate-900 text-slate-400 hover:text-white border border-slate-800'}`}
          >
            Projects ({counts.project})
          </button>
          <button
            onClick={() => setActiveFilter('hackathon')}
            className={`text-[10px] px-2.5 py-1 rounded-md font-semibold transition-all ${activeFilter === 'hackathon' ? 'bg-amber-600 text-white shadow-md' : 'bg-slate-900 text-slate-400 hover:text-white border border-slate-800'}`}
          >
            Hackathons ({counts.hackathon})
          </button>
        </div>
      </div>

      {/* Activity Timeline List */}
      <div className="flex-1 space-y-4 overflow-y-auto pr-1 custom-scrollbar max-h-[520px]">
        {filteredEvents.length === 0 ? (
          <div className="text-center py-10 text-slate-500 text-xs">
            No activity events found for category "{activeFilter}".
          </div>
        ) : (
          filteredEvents.map((item, idx) => (
            <div key={idx} className="flex gap-3.5 items-start relative pl-4 border-l border-slate-800/80 group">
              {/* Timeline Dot */}
              <div className="absolute -left-[7px] top-1.5 w-3 h-3 rounded-full bg-slate-950 border-2 border-indigo-500 group-hover:border-emerald-400 transition-colors" />

              {/* Event Card */}
              <div className="bg-slate-900/90 border border-slate-800/90 group-hover:border-slate-700 p-4 rounded-xl flex-1 space-y-2.5 shadow-md transition-all">
                <div className="flex flex-wrap items-center justify-between gap-2">
                  <div className="flex items-center gap-2">
                    <span className="p-1.5 rounded-lg bg-slate-950 border border-slate-800">{getCategoryIcon(item.category)}</span>
                    <span className="text-xs font-mono font-extrabold text-indigo-400">{item.date || item.year}</span>
                  </div>
                  {getCategoryBadge(item.category)}
                </div>

                {/* Title */}
                <h4 className="text-xs font-bold text-white group-hover:text-indigo-200 transition-colors leading-snug">
                  {item.event}
                </h4>

                {/* Content Snippet / Post Text */}
                {item.content && (
                  <p className="text-[11px] text-slate-300 bg-slate-950/70 p-2.5 rounded-lg border border-slate-800/80 leading-relaxed font-normal">
                    "{item.content}"
                  </p>
                )}

                {/* Footer Engagement Metrics & URL Link */}
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
                      className="inline-flex items-center gap-1 text-indigo-400 hover:text-indigo-300 font-semibold"
                    >
                      <span>View Source</span>
                      <ExternalLink className="w-2.5 h-2.5" />
                    </a>
                  )}
                </div>
              </div>
            </div>
          ))
        )}
      </div>
    </div>
  );
}
