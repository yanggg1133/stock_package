from openerp.osv import osv, fields

class StockOutPackage(osv.osv):
    _name = 'stock.out.package'

    _columns = {
        'name': fields.char('Name'),
	'picking': fields.many2one('stock.picking', 'Delivery Order'),
	'tracking_number': fields.char('Tracking Number'),
	'weight': fields.float('Package Weight'),
    }
