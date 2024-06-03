import express from "express";

const app = express();

const router = express.Router();

app.use("/api", router);

router.get("/hello", (req: any, res: any) => {
  res.json({
    message: "Hello, world!",
  });
});

app.listen(3999, () => {
  console.log("Server is running at http://localhost:3999");
});
