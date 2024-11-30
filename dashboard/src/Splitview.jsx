import React, { useState } from "react";
import axios from "axios";

const SplitView = () => {
  const [message, setMessage] = useState("");
  const [response, setResponse] = useState("");

  // Function to send a prompt to the other app
  const sendPrompt = async () => {
    try {
      const result = await axios.post("http://127.0.0.1:5000/chatbot", {
        prompt: message,
      });
      setResponse(result.data.message);
      console.log(result.data.message); 
      setMessage("");
    } catch (error) {
      console.error("Error sending prompt:", error);
    }
  };

  return (
    <div className="flex h-screen">
      {/* Left Panel - Embedded App */}
      <div className="w-4/5 border-r">
        <iframe
          src="http://localhost:1313"
          className="w-full h-full"
          // style={{ all: "initial" }}
          sandbox="allow-scripts allow-same-origin allow-forms allow-modals"
          title="Embedded App"
        ></iframe>
      </div>

      {/* Right Panel - Chatbot Interface */}
      <div className="w-1/4 p-4 bg-white shadow-lg h-screen flex flex-col rounded-lg">
        <h1 className="text-2xl font-bold mb-6 text-blue-600 text-center">
          Chatbot
        </h1>
        <div className="flex-1 overflow-y-auto p-4 border border-gray-300 rounded-lg bg-gray-50">
          {response && response.map((res, index) => (
            <div key={index} className="mt-4 p-3 border border-gray-200 rounded-lg bg-white shadow-sm">
              <p className="text-gray-600">Tag: {res.tag}</p>
              <p className="font-bold text-gray-800">Content: {res.content}</p>
            </div>
          ))}
        </div>
        <div className="flex items-center p-2 border-t border-gray-300">
          <textarea
            className="w-full h-16 p-3 border border-gray-300 rounded-lg resize-none focus:outline-none focus:ring-2 focus:ring-blue-500"
            placeholder="Type your message..."
            value={message}
            onChange={(e) => setMessage(e.target.value)}
          />
          <button
            className="ml-2 w-24 bg-blue-600 text-white py-2 rounded-lg hover:bg-blue-700 transition duration-200"
            onClick={sendPrompt}
          >
            Send
          </button>
        </div>
      </div>
    </div>
  );
};

export default SplitView;
