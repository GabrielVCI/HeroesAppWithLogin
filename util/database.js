const Sequelize = require("sequelize");
const path = require("path");

 const sequelize = new Sequelize("HeroesAppWithLogin", "sa", "RA1708222612gr", {
  dialect: "mssql",
  host: "localhost",
  

}); 
/* 
const sequelize = new Sequelize("sqlite::memory:", {
  dialect: "sqlite",
  storage: path.join(path.dirname(require.main.filename),"heroesapp.sqlite"),
}); */

module.exports = sequelize;
