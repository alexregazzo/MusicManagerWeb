(this["webpackJsonpmusic-manager-web"]=this["webpackJsonpmusic-manager-web"]||[]).push([[0],{30:function(e,t,n){"use strict";n.r(t);var c=n(0),r=n.n(c),s=n(13),o=n.n(s),i=n(14),a=n(2),u=n(8),j=n(1),b=Object(c.createContext)(),d=function(e){var t=e.children,n=Object(c.useState)(null),r=Object(u.a)(n,2),s=r[0],o=r[1];return Object(j.jsx)(b.Provider,{value:{signedIn:!!s,setUserId:o,userId:s},children:t})},h=b;var l=function(){var e=Object(c.useContext)(h),t=e.signedIn,n=e.userId,r=e.setUserId,s=Object(c.useState)(""),o=Object(u.a)(s,2),i=o[0],a=o[1],b=Object(c.useState)(""),d=Object(u.a)(b,2),l=d[0],O=d[1],f=Object(c.useState)(null),x=Object(u.a)(f,2),p=x[0],g=x[1],m=Object(c.useState)(null),v=Object(u.a)(m,2),y=v[0],S=v[1];return Object(c.useEffect)((function(){if(!n)return;fetch("/api/v0/spotify/isconnected?id=".concat(n),{method:"GET"}).then((function(e){return e.ok?e.json():{}})).then((function(e){g(e.is_connected),S(e.connect_link)}))}),[n]),t?(console.log(n),Object(j.jsxs)("div",{children:[null!==p&&!p&&Object(j.jsx)("a",{href:y,children:"Conectar ao Spotify"}),Object(j.jsxs)("h2",{children:["Teste ",n]})]})):Object(j.jsx)("div",{children:Object(j.jsxs)("form",{children:[Object(j.jsx)("h3",{children:"Entrar/Cadastrar"}),Object(j.jsx)("label",{children:"Username:"}),Object(j.jsx)("input",{type:"text",onChange:function(e){return a(e.target.value)}}),Object(j.jsx)("label",{children:"Password:"}),Object(j.jsx)("input",{type:"password",onChange:function(e){return O(e.target.value)}}),Object(j.jsx)("button",{type:"button",onClick:function(){fetch("/api/v0/account/signup",{method:"POST",body:JSON.stringify({username:i,password:l})}).then((function(e){return e.ok?e.json():{}})).then((function(e){r(e.use_id)}))},children:"Cadastrar"}),Object(j.jsx)("button",{type:"button",onClick:function(){fetch("/api/v0/account/login",{method:"POST",body:JSON.stringify({username:i,password:l})}).then((function(e){return e.ok?e.json():{}})).then((function(e){console.log(e),r(e.use_id)}))},children:"Entrar"})]})})};var O=function(){return Object(j.jsx)("h2",{children:"Testing"})};var f=function(){return Object(j.jsx)("h2",{children:"Testing"})};var x=function(){return Object(j.jsx)(d,{children:Object(j.jsxs)(i.a,{children:[Object(j.jsx)(a.a,{exact:!0,path:"/",component:l}),Object(j.jsx)(a.a,{exact:!0,path:"/signup",component:f}),Object(j.jsx)(a.a,{exact:!0,path:"/login",component:O})]})})};o.a.render(Object(j.jsx)(r.a.StrictMode,{children:Object(j.jsx)(x,{})}),document.getElementById("root"))}},[[30,1,2]]]);
//# sourceMappingURL=main.2f0f3c6b.chunk.js.map