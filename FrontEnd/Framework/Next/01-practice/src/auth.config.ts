import type { NextAuthConfig } from "next-auth";

export const authConfig = {
  pages: {
    // signIn: "/login",
  },
  callbacks: {
    authorized({ request: { nextUrl }, auth }) {
      console.log("🚀 ~ auth.config.ts ~ auth:", auth);
      const isLoggedIn = !!auth?.user;
      if (!isLoggedIn) {
        return false;
      }
      return true;
    },
    signIn({ profile, user }) {
      return true;
    },
  },
  providers: [], // Add providers with an empty array for now
} satisfies NextAuthConfig;
