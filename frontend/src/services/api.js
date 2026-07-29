import axios from "axios";

const api = axios.create({
    baseURL: "https://driver-recommendation-agent.onrender.com",
});

export const assignDriver = (payload) => api.post("/assign-driver", payload);

export default api;