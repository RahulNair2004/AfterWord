import { Link, Outlet } from "react-router-dom";

const navLinks = [
  { label: "Home", to: "/" },
  { label: "Explore Cases", to: "/cases" },
  { label: "Login", to: "/login" },
  { label: "Register", to: "/register" },
];

export default function MainLayout() {
  return (
    <div className="min-h-screen flex flex-col bg-white text-gray-900">
      <nav className="border-b border-gray-200">
        <div className="mx-auto flex max-w-6xl items-center justify-between px-4 py-4">
          <Link to="/" className="text-xl font-semibold">
            AfterWord
          </Link>

          <ul className="flex items-center gap-6 text-sm">
            {navLinks.map((item) => (
              <li key={item.to}>
                <Link to={item.to} className="hover:underline">
                  {item.label}
                </Link>
              </li>
            ))}
          </ul>
        </div>
      </nav>

      <main className="mx-auto w-full max-w-6xl flex-1 px-4 py-8">
        <Outlet />
      </main>
    </div>
  );
}