from odoo import models, fields, api

class CommandeClient(models.Model):
    _name = "commande.client"
    _description = "Commande Client"

    name = fields.Char(string="Nom du client", required=True)
    produit = fields.Char(string="Produit", required=True)
    quantite = fields.Integer(string="Quantité", default=1)
    statut = fields.Selection([
        ('brouillon', 'Brouillon'),
        ('validee', 'Validée'),
        ('envoyee', 'Envoyée'),
    ], string="Statut", default='brouillon')
    date_commande = fields.Date(string="Date de commande", required=True)
    prix_unitaire = fields.Float(string="Prix unitaire", default=10.0)
    prix_total = fields.Float(string="Prix total", compute="_compute_prix_total", store=True)

    @api.depends('quantite', 'prix_unitaire')
    def _compute_prix_total(self):
        for record in self:
            record.prix_total = record.quantite * record.prix_unitaire

    def action_valider(self):
        for record in self:
            if record.statut == 'brouillon':
                record.statut = 'validee'
