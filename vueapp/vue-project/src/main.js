import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";

import "./assets/Main.css";

import mitt from "mitt"
const emitter = mitt();
const app = createApp(App);
const domain = "docker.data.techcollege.dk"
const port = 30010
const webapi_url = `http://${domain}:${port}/`
export { webapi_url }
app.use(router);
app.config.globalProperties.emitter = emitter;
app.config.globalProperties.webapi_url = webapi_url;
app.mount("#app");
