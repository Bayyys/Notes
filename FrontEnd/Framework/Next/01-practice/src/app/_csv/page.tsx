"use client";
import React, { useState } from "react";
import Papa from "papaparse";

export default function Page() {
  const [data, setData] = useState<any[]>([]);

  const handleFileSelect = (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0]; // Add null check
    if (file) {
      const reader = new FileReader();
      reader.onload = (event) => {
        const csvData = event.target?.result;
        const parsedData: any[] = Papa.parse(csvData as string).data;

        console.log("🚀 ~ handleFileSelect ~ parsedData:", parsedData);

        setData(parsedData);
      };
      reader.readAsText(file);
    }
  };

  return (
    <div>
      <input type="file" onChange={handleFileSelect} />
      <table>
        <tbody>
          {data.map((row: any[], index) => (
            <tr key={index}>
              {row.map((cell, index) => (
                <td key={index}>{cell}</td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
