import App from "./App";
import Admin from "./pages/Admin";
import Users from "./pages/Users";

const routes = [
    {     
        path: "/",
        component: App,
        name: "App",
        meta: { title: "David&CIA" },
    }, 
    {     
        path: "/admin",
        component: Admin,
        name: "Admin",
        meta: { title: "David&CIA - Admin" },
    }, 
    {     
        path: "/users",
        component: Users,
        name: "Users",
        meta: { title: "David&CIA - Users" },
    }, 
];
export default routes;