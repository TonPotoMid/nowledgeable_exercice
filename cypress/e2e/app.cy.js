describe("Application web - parcours reel", () => {
  it("l'application est disponible sur la page d'accueil", () => {
    cy.request("/").its("status").should("eq", 200);
  });

  it("le endpoint /health repond OK", () => {
    cy.request("/health").then((response) => {
      expect(response.status).to.eq(200);
      expect(response.body).to.deep.equal({ status: "ok" });
    });
  });

  it("le endpoint /api/items retourne une liste d'items", () => {
    cy.request("/api/items").then((response) => {
      expect(response.status).to.eq(200);
      expect(response.body).to.have.property("items");
      expect(response.body.items).to.be.an("array").and.not.be.empty;
    });
  });
});
