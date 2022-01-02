import App from "./App";
import Admin from "./pages/Admin";
import Users from "./pages/Users";
import Materials from "./pages/Materials";
import Agenda from "./pages/Agenda";

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
        meta: { title: "David&CIA - Administracion" },
    }, 
    {     
        path: "/users",
        component: Users,
        name: "Users",
        meta: { title: "David&CIA - Usuarios" },
    }, 
    {     
        path: "/materials",
        component: Materials,
        name: "Materials",
        meta: { title: "David&CIA - Materiales" },
    }, 
    {     
        path: "/agenda",
        component: Agenda,
        name: "Agenda",
        meta: { title: "David&CIA - Agenda" },
    }, 
];
export default routes;