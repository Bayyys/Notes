import NextAuth from "next-auth";
import Credentials from "next-auth/providers/credentials";
import { authConfig } from "./auth.config";
import { z } from "zod";
import { userAgent } from "next/server";

export const { handlers, auth, signIn, signOut } = NextAuth({
  ...authConfig,
  providers: [
    Credentials({
      credentials: {
        username: { label: "用户名" },
        password: { label: "密码", type: "password" },
      },
      authorize: async (credentials, request) => {
        let user = null;

        // logic to salt and hash password
        const pwHash = z.string().parse(credentials.password);
        user = { name: "bayyy", email: "123@qq.com", age: 18 };
        return user;
      },
    }),
  ],
});
