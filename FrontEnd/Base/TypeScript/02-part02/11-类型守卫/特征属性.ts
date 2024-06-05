interface Download {
  type: "download";
  filename: string;
}

interface Upload {
  type: "upload";
  url: string;
}

type MyRequest = Download | Upload;

const handleRequest = (request: MyRequest) => {
  switch (request.type) {
    case "download":
      console.log(request.filename);
      break;
    case "upload":
      console.log(request.url);
      break;
    default:
      throw new Error("unsupported type");
  }
};
