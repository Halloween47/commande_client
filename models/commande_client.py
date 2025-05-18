from odoo import models, fields

class CommandeClient(models.Model):
    _name = "commande.client"
    _description = "Commande Client"

    name = fields.Char(string="Référence", required=True)
    produit = fields.Char(string="Produit")
    quantite = fields.Integer(string="Quantité")
    prix_unitaire = fields.Float(string="Prix Unitaire")
    prix_total = fields.Float(string="Prix Total", compute="_compute_prix_total", store=True)
    date_commande = fields.Date(string="Date de Commande")
    statut = fields.Selection([
        ('brouillon', 'Brouillon'),
        ('validee', 'Validée'),
        ('envoyee', 'Envoyée')
    ], default='brouillon', string="Statut")

    @staticmethod
    def _compute_prix_total(self):
        for record in self:
            record.prix_total = record.quantite * record.prix_unitaire
    
    def action_valider(self):
        for record in self:
            if record.statut == 'brouillon':
                record.statut = 'validee'