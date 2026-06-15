"use client";

import { useState } from "react";
import axios from "axios";

export default function FileUpload() {
  const [file, setFile] = useState<File | null>(null);
  const [message, setMessage] = useState("");

  const uploadFile = async () => {
    if (!file) return;

    const formData = new FormData();

    formData.append(
      "file",
      file
    );

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/upload",
        formData,
        {
          headers: {
            "Content-Type":
              "multipart/form-data",
          },
        }
      );

      setMessage(
        response.data.message
      );

    } catch (error) {
      console.error(error);

      setMessage(
        "Upload failed"
      );
    }
  };

  return (
    <div className="border rounded p-5 space-y-4">

      <h2 className="text-xl font-semibold">
        Upload Business Documents
      </h2>

      <input
        type="file"
        onChange={(e) =>
          setFile(
            e.target.files?.[0] || null
          )
        }
      />

      <button
        onClick={uploadFile}
        className="bg-blue-600 text-white px-4 py-2 rounded"
      >
        Upload
      </button>

      {message && (
        <p className="text-green-500">
          {message}
        </p>
      )}

    </div>
  );
}