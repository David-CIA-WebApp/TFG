import Admin from "./pages/Admin";
import App from "./App";

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
];
export default routes;