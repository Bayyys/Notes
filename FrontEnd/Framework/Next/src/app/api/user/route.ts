// GET 方法: 返回{code: 200, msg: 'Hello World!'}

import { PrismaClient } from "@prisma/client";
import { NextRequest, NextResponse } from "next/server";

const prisma = new PrismaClient();

export const GET = async (req: NextRequest) => {
  const params = req.nextUrl.searchParams;
  const id_query = params.get("id");
  const id = parseInt(id_query ?? "0");
  const name_query = params.get("name");
  const name = name_query ?? "";
  const res = await prisma.user.findMany({
    where: {
      id: id ? { equals: id } : undefined,
      name: name ? { equals: name } : undefined,
    },
  });

  return NextResponse.json({ code: 200, msg: "success", data: res });
};
