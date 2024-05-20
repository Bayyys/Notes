import Link from "next/link";

export default function Home() {
  return (
    <>
      <Link href="/logout">Logout</Link>
      <Link href="/csv">CSV</Link>
    </>
  );
}
