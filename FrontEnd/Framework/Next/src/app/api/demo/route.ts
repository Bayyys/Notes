// GET 方法: 返回{code: 200, msg: 'Hello World!'}

import { NextRequest, NextResponse } from "next/server";
import { PrismaClient } from "@prisma/client";

export const GET = async () => {
  const prisma = new PrismaClient();
  await prisma.user.create({
    data: {
      name: "bayyy",
      age: 24,
      sex: true,
      email: "123@qq.com",
      tel: "110",
    },
  });
  const data = await prisma.user.findMany();
  return NextResponse.json({ code: 200, data });
};

export const POST = async (req: NextRequest) => {
  let data = await req.json();
  data = {};
  const params = req.nextUrl.searchParams;

  console.log("🚀 ~ POST ~ data:", req.url, params.get("1"));

  const prisma = new PrismaClient();
  if (!data.name) {
    return NextResponse.json({ code: 400, msg: "name is required" });
  }
  const sus = await prisma.user.create({
    data,
  });
  return NextResponse.json({ code: 200, msg: "success", data: sus });
};
