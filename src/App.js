import { BrowserRouter, Route } from "react-router-dom";
import { AuthProvider } from "./context/auth";
import Dashboard from "./pages/dashboard";
import Login from "./pages/login";
import Signup from "./pages/signup";

function App() {
  return (
    <AuthProvider>
      <BrowserRouter>
        <Route exact path="/" component={Dashboard} />
        <Route exact path="/signup" component={Signup} />
        <Route exact path="/login" component={Login} />
      </BrowserRouter>
    </AuthProvider>
  );
}

export default App;
