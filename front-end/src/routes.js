import Public from "./pages/Public";
import Admin from "./pages/Admin";
import Users from "./pages/Users";
import UserDetail from "./pages/UserDetail";
import Materials from "./pages/Materials";
import Jobs from "./pages/Jobs";
import Agenda from "./pages/Agenda";
import Alertas from "./pages/Alertas";
import Consultas from "./pages/Consultas";

const routes = [
    {     
        path: "/",
        component: Public,
        name: "Public",
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
        path: "/user/:id",
        component: UserDetail,
        name: "UserDetail",
        meta: { title: "David&CIA - Usuario" },
    }, 
    {     
        path: "/materials",
        component: Materials,
        name: "Materials",
        meta: { title: "David&CIA - Materiales" },
    }, 
    {     
        path: "/jobs",
        component: Jobs,
        name: "Jobs",
        meta: { title: "David&CIA - Trabajos" },
    }, 
    {     
        path: "/jobs/:id",
        component: Jobs,
        name: "Jobs",
        meta: { title: "David&CIA - Trabajos" },
    }, 
    {     
        path: "/agenda",
        component: Agenda,
        name: "Agenda",
        meta: { title: "David&CIA - Agenda" },
    }, 
    {     
        path: "/alertas",
        component: Alertas,
        name: "Alertas",
        meta: { title: "David&CIA - Alertas" },
    }, 
    {     
        path: "/consultas",
        component: Consultas,
        name: "Consultas",
        meta: { title: "David&CIA - Consultas" },
    }, 
];
export default routes;