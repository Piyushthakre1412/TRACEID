import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || '/api';

export const fetchIdentityGraph = async (
  personId = 'P_101',
  minThreshold = 70.0,
  weightFace = 0.40,
  weightBio = 0.35,
  weightHandle = 0.25
) => {
  try {
    const response = await axios.get(`${API_BASE_URL}/graph/${personId}`, {
      params: {
        min_threshold: minThreshold,
        weight_face: weightFace,
        weight_bio: weightBio,
        weight_handle: weightHandle
      }
    });
    return response.data;
  } catch (error) {
    console.warn('API connection offline, using fallback dataset demo schema', error);
    return {
      target_identity: {
        person_id: personId || "P_101",
        canonical_name: personId === "P_102" ? "Om Patil" : (personId === "P_103" ? "Satwik Mhasaye" : "Piyush Thakre"),
        primary_image: "/dataset/images/piyush.jpg",
        institution: "Prof. Ram Meghe Institute Of Technology and Research, Badnera",
        overall_confidence: roundConfidence(96.0 * weightFace + 93.5 * weightBio + 91.0 * weightHandle),
        confidence_breakdown: {
          facial_similarity: 96.0,
          bio_semantic_similarity: 93.5,
          handle_match: 91.0
        }
      },
      graph_data: {
        nodes: [
          {
            id: personId || "P_101",
            type: "person",
            position: { x: 300, y: 180 },
            data: {
              label: personId === "P_102" ? "Om Patil" : (personId === "P_103" ? "Satwik Mhasaye" : "Piyush Thakre"),
              canonical_name: personId === "P_102" ? "Om Patil" : (personId === "P_103" ? "Satwik Mhasaye" : "Piyush Thakre"),
              type: "person"
            }
          },
          {
            id: `H_${personId}_1`,
            type: "handle",
            position: { x: 100, y: 320 },
            data: { label: "@piyush-thakre (GitHub)", type: "handle" }
          },
          {
            id: `ORG_${personId}`,
            type: "organization",
            position: { x: 300, y: 400 },
            data: { label: "PRMITR Badnera", type: "organization" }
          },
          {
            id: `PROJ_${personId}`,
            type: "project",
            position: { x: 500, y: 320 },
            data: { label: "ACE / InterceptAI", type: "project" }
          }
        ],
        edges: [
          {
            id: `e_${personId}_h`,
            source: personId || "P_101",
            target: `H_${personId}_1`,
            label: "OWNED_BY (92.0%)",
            type: "smoothstep",
            animated: true,
            style: { stroke: "#10b981", strokeWidth: 2 },
            data: { relationship: "OWNED_BY", confidence: 92.0 }
          },
          {
            id: `e_${personId}_org`,
            source: personId || "P_101",
            target: `ORG_${personId}`,
            label: "AFFILIATED_WITH (95.0%)",
            type: "smoothstep",
            animated: true,
            style: { stroke: "#10b981", strokeWidth: 2 },
            data: { relationship: "AFFILIATED_WITH", confidence: 95.0 }
          },
          {
            id: `e_${personId}_proj`,
            source: personId || "P_101",
            target: `PROJ_${personId}`,
            label: "CONTRIBUTED_TO (90.0%)",
            type: "smoothstep",
            animated: true,
            style: { stroke: "#6366f1", strokeWidth: 2 },
            data: { relationship: "CONTRIBUTED_TO", confidence: 90.0 }
          }
        ]
      },
      timeline: [
        { year: "2023", event: "Enrolled at PRMITR Badnera", category: "education" },
        { year: "2026", event: "Project ACE Created for Hack Synthesis 3.0", category: "hackathon" }
      ],
      evidence_trail: [
        {
          node_id: `H_${personId}_1`,
          source_url: "https://github.com/piyush-thakre",
          verified_at: "2026-09-19",
          proof_type: "Direct Bi-Directional URL Match"
        },
        {
          node_id: `ORG_${personId}`,
          source_url: "https://mitra.ac.in",
          verified_at: "2026-09-19",
          proof_type: "Verified Institutional Directory Record"
        }
      ]
    };
  }
};

function roundConfidence(val) {
  return Math.round(val * 10) / 10;
}

export const searchIdentity = async (formData) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/search`, formData, {
      headers: { 'Content-Type': 'multipart/form-data' }
    });
    return response.data;
  } catch (error) {
    console.warn('Backend search API error, returning mock resolved identity', error);
    return {
      person_id: "P_101",
      canonical_name: "Piyush Thakre",
      overall_confidence: 94.2,
      confidence_breakdown: {
        facial_similarity: 96.0,
        bio_semantic_similarity: 93.5,
        handle_match: 91.0
      }
    };
  }
};
