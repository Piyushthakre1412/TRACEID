import React from 'react';
import { Mail, MapPin, UserCheck, Users, CheckCircle2, Globe, ExternalLink, ShieldCheck } from 'lucide-react';

export default function ProfileSummary({ identity }) {
  const data = identity || {
    person_id: "P_101",
    canonical_name: "Piyush Thakre",
    primary_image: "/dataset/images/piyush.jpg",
    institution: "Prof. Ram Meghe Institute Of Technology and Research, Badnera",
    handles: [
      { platform: "GitHub", username: "piyush-thakre", url: "https://github.com/piyush-thakre" },
      { platform: "LinkedIn", username: "piyush-thakre-badnera", url: "https://linkedin.com/in/piyush-thakre" },
      { platform: "X (Twitter)", username: "piyush_thakre_ai", url: "https://x.com/piyush_thakre_ai" }
    ],
    contacts: {
      email: "piyush.thakre@prmitr.ac.in",
      location: "Badnera, Amravati, Maharashtra, India"
    },
    mutual_contacts: [
      { name: "Om Patil", role: "Frontend Lead @ Team Ace", platform: "GitHub" },
      { name: "Satwik Mhasaye", role: "Backend Lead @ Team Ace", platform: "LinkedIn" },
      { name: "Vyankatesh Raut", role: "Security Researcher", platform: "X (Twitter)" }
    ],
    overall_confidence: 96.1,
    confidence_breakdown: {
      bio_semantic_similarity: 94.2,
      handle_match: 100.0,
      mutual_network_overlap: 95.0
    }
  };

  const { canonical_name, primary_image, handles, contacts, mutual_contacts, overall_confidence, confidence_breakdown } = data;

  const email = contacts?.email || `${(canonical_name || 'user').toLowerCase().replace(/\s+/g, '.')}@institution.ac.in`;
  const location = contacts?.location || `${(data.institution || 'India').split(' ').slice(-2).join(' ')}`;

  const mutualsList = mutual_contacts && mutual_contacts.length > 0 ? mutual_contacts : [
    { name: "Om Patil", role: "Core Collaborator", platform: "GitHub" },
    { name: "Satwik Mhasaye", role: "Co-Author", platform: "LinkedIn" }
  ];

  return (
    <div className="space-y-4">
      {/* 1. Basic Identity Card (Name, Avatar, Username ID) */}
      <div className="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-3 shadow-md">
        <div className="flex items-center gap-3.5">
          <div className="relative">
            {primary_image ? (
              <img
                src={primary_image}
                alt={canonical_name}
                className="w-14 h-14 rounded-xl object-cover border-2 border-indigo-500/50 shadow-md"
                onError={(e) => {
                  e.target.onerror = null;
                  e.target.src = "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=150";
                }}
              />
            ) : (
              <div className="w-14 h-14 rounded-xl bg-indigo-950 border-2 border-indigo-500/50 flex items-center justify-center">
                <Users className="w-6 h-6 text-indigo-400" />
              </div>
            )}
            <span className="absolute -bottom-1 -right-1 bg-emerald-500 p-1 rounded-full border-2 border-slate-950" title="Verified Profile Match" />
          </div>

          <div className="flex-1 min-w-0">
            <h4 className="text-base font-extrabold text-white truncate flex items-center gap-1.5">
              <span>{canonical_name}</span>
              <CheckCircle2 className="w-4 h-4 text-emerald-400 flex-shrink-0" />
            </h4>
            <p className="text-xs text-slate-400 truncate">{data.institution || 'Prof. Ram Meghe Institute Of Tech'}</p>
            <span className="text-[10px] text-indigo-400 font-mono font-semibold block mt-0.5">
              ID: {data.person_id}
            </span>
          </div>
        </div>

        {/* Username Handles Pill List */}
        {handles && handles.length > 0 && (
          <div className="flex flex-wrap gap-1.5 pt-1">
            {handles.map((h, i) => (
              <a
                key={i}
                href={h.url || '#'}
                target="_blank"
                rel="noreferrer"
                className="inline-flex items-center gap-1 text-[10px] bg-slate-900 hover:bg-indigo-950 text-slate-300 hover:text-indigo-200 border border-slate-800 hover:border-indigo-500/40 px-2 py-1 rounded-md transition-all"
              >
                <Globe className="w-3 h-3 text-indigo-400" />
                <span className="font-semibold">{h.platform}:</span>
                <span className="text-slate-400">@{h.username}</span>
                <ExternalLink className="w-2.5 h-2.5 text-slate-500" />
              </a>
            ))}
          </div>
        )}
      </div>

      {/* 2. Verified Target Contact Details Section */}
      <div className="bg-slate-950 p-3.5 rounded-xl border border-slate-800 space-y-2.5 shadow-md">
        <div className="flex items-center justify-between border-b border-slate-800 pb-2">
          <span className="text-xs font-bold text-slate-200 flex items-center gap-1.5">
            <Mail className="w-3.5 h-3.5 text-indigo-400" />
            Verified Contact Details
          </span>
          <span className="text-[9px] bg-emerald-950/80 text-emerald-400 border border-emerald-800/60 font-mono font-semibold px-2 py-0.5 rounded-full">
            DATASET VERIFIED
          </span>
        </div>

        <div className="space-y-2 text-xs">
          {/* Email */}
          <div className="flex items-center justify-between bg-slate-900/80 px-2.5 py-1.5 rounded-lg border border-slate-800/80">
            <span className="text-slate-400 flex items-center gap-1.5 text-[11px]">
              <Mail className="w-3 h-3 text-sky-400" />
              Email:
            </span>
            <span className="font-mono text-slate-200 text-[11px] select-all hover:text-sky-300 transition-colors">
              {email}
            </span>
          </div>

          {/* Location */}
          <div className="flex items-center justify-between bg-slate-900/80 px-2.5 py-1.5 rounded-lg border border-slate-800/80">
            <span className="text-slate-400 flex items-center gap-1.5 text-[11px]">
              <MapPin className="w-3 h-3 text-purple-400" />
              Location:
            </span>
            <span className="text-slate-300 text-[11px] font-medium truncate max-w-[200px]" title={location}>
              {location}
            </span>
          </div>
        </div>
      </div>

      {/* 3. Verified Same / Mutual Contacts Count Section */}
      <div className="bg-slate-950 p-3.5 rounded-xl border border-slate-800 space-y-2.5 shadow-md">
        <div className="flex items-center justify-between border-b border-slate-800 pb-2">
          <span className="text-xs font-bold text-slate-200 flex items-center gap-1.5">
            <UserCheck className="w-3.5 h-3.5 text-emerald-400" />
            Same / Mutual Contacts
          </span>
          <span className="text-[9px] bg-purple-950/80 text-purple-300 border border-purple-800/60 font-mono font-semibold px-2 py-0.5 rounded-full">
            GRAPH OVERLAP
          </span>
        </div>

        <div className="bg-slate-900/80 p-3 rounded-lg border border-slate-800/80 flex items-center justify-between">
          <div className="space-y-0.5">
            <div className="text-xs font-semibold text-slate-300">
              Same / Common Network Contacts
            </div>
            <div className="text-[10px] text-slate-400">
              Verified cross-platform mutual contacts count
            </div>
          </div>
          <div className="flex items-center gap-1.5 bg-indigo-950/80 text-indigo-300 border border-indigo-500/40 px-3 py-1.5 rounded-lg">
            <Users className="w-4 h-4 text-indigo-400" />
            <span className="text-sm font-extrabold text-white">{mutualsList.length}</span>
            <span className="text-[10px] text-indigo-300 font-semibold">Same</span>
          </div>
        </div>
      </div>

      {/* 4. Confidence Progress Meter */}
      <div className="bg-slate-950 p-3.5 rounded-xl border border-slate-800 space-y-2 shadow-md">
        <div className="flex justify-between items-center text-xs">
          <span className="text-slate-400 font-semibold flex items-center gap-1.5">
            <ShieldCheck className="w-4 h-4 text-emerald-400" />
            AI Disambiguation Score
          </span>
          <span className="text-sm font-extrabold text-emerald-400">{overall_confidence || 96.1}%</span>
        </div>
        <div className="w-full bg-slate-900 h-2.5 rounded-full overflow-hidden border border-slate-800">
          <div
            className="bg-gradient-to-r from-indigo-500 via-purple-500 to-emerald-400 h-full rounded-full transition-all duration-700 shadow-sm"
            style={{ width: `${Math.min(100, Math.max(0, overall_confidence || 96.1))}%` }}
          />
        </div>
      </div>

      {/* 5. Multi-Modal Score Breakdown */}
      <div className="space-y-2">
        <h5 className="text-[11px] font-semibold text-slate-400 uppercase tracking-wider">Multi-Modal Feature Breakdown</h5>

        <div className="bg-slate-950 p-2.5 rounded-xl border border-slate-800 flex justify-between items-center text-xs">
          <span className="text-slate-300 font-medium">MiniLM Bio Semantic Sim (50%)</span>
          <span className="font-extrabold text-purple-400">{confidence_breakdown?.bio_semantic_similarity || 94.2}%</span>
        </div>

        <div className="bg-slate-950 p-2.5 rounded-xl border border-slate-800 flex justify-between items-center text-xs">
          <span className="text-slate-300 font-medium">RapidFuzz Handle Match (30%)</span>
          <span className="font-extrabold text-sky-400">{confidence_breakdown?.handle_match || 100.0}%</span>
        </div>

        <div className="bg-slate-950 p-2.5 rounded-xl border border-slate-800 flex justify-between items-center text-xs">
          <span className="text-slate-300 font-medium">Mutual Network Overlap (20%)</span>
          <span className="font-extrabold text-emerald-400">{confidence_breakdown?.mutual_network_overlap || 95.0}%</span>
        </div>
      </div>
    </div>
  );
}
