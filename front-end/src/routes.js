import App from "./App";
import Admin from "./pages/Admin";
import Users from "./pages/Users";
import Materials from "./pages/Materials";

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
    {     
        path: "/materials",
        component: Materials,
        name: "Materials",
        meta: { title: "David&CIA - Materials" },
    }, 
];
export default routes;