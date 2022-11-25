from odoo import api, fields, models


class AccountMoveInherit(models.Model):
    _inherit = 'account.move'


    @api.onchange('invoice_line_ids')
    def _onchange_lines(self):
        pass
        # line_lst = []
        # total_amount = 0.0
        # for line in self.invoice_line_ids:
        #     if line_lst:
        #         exist = list(filter(lambda i: i if i['design_id'] == line.product_id.categ_id.id and i[
        #             'quality_id'] == line.quality_id.id else None, line_lst))
        #         if exist:
        #             line.price_unit = exist[0]['price']
        #             line.price_subtotal = exist[0]['price'] * exist[0]['quantity']
        #             total_amount += exist[0]['price'] * exist[0]['quantity']
        #             self._compute_amount()
        #
        #         else:
        #             line_lst.append({
        #                 'product_id': line.product_id.id,
        #                 'design_id': line.product_id.categ_id.id,
        #                 'quality_id': line.quality_id.id,
        #                 'price': line.price_unit,
        #                 'quantity': line.quantity,
        #                 'price_subtotal': line.price_subtotal,
        #             })
        #             total_amount += line.price_subtotal
        #             for item in self.line_ids:
        #                 line_exist = list(filter(lambda i: i if i['design_id'] == item.product_id.categ_id.id and i[
        #                     'quality_id'] == item.product_id.carpet_quality_id.id else None, line_lst))
        #                 if line_exist:
        #                     item.credit = line_exist[0]['price'] * line_exist[0]['quantity']
        #     else:
        #         line_lst.append({
        #             'product_id': line.product_id.id,
        #             'design_id': line.product_id.categ_id.id,
        #             'quality_id': line.quality_id.id,
        #             'price': line.price_unit,
        #             'quantity': line.quantity,
        #             'price_subtotal': line.price_subtotal,
        #         })
        #         total_amount += line.price_subtotal
        # return total_amount
                # for item in self.line_ids:
                #     if line.product_id.id == item.product_id.id:
                #         item.credit = line.quantity * line.price_unit
                #         item.credit = line.quantity * line.price_unit


    # def _compute_amount(self):
    #     line_lst = []
    #     total_amount = 0.0
    #     total_debit = 0.0
    #     for line in self.invoice_line_ids:
    #         if line_lst:
    #             exist = list(filter(lambda i: i if i['design_id'] == line.product_id.categ_id.id and i[
    #                 'quality_id'] == line.quality_id.id else None, line_lst))
    #             if exist:
    #                 line.price_unit = exist[0]['price']
    #                 line.price_subtotal = exist[0]['price'] * exist[0]['quantity']
    #                 total_amount += exist[0]['price'] * exist[0]['quantity']
    #
    #
    #             else:
    #                 line_lst.append({
    #                     'product_id': line.product_id.id,
    #                     'design_id': line.product_id.categ_id.id,
    #                     'quality_id': line.quality_id.id,
    #                     'price': line.price_unit,
    #                     'quantity': line.quantity,
    #                     'price_subtotal': line.price_subtotal,
    #                 })
    #                 total_amount += line.price_subtotal
    #                 for item in self.line_ids:
    #                     line_exist = list(filter(lambda i: i if i['design_id'] == item.product_id.categ_id.id and i[
    #                         'quality_id'] == item.product_id.carpet_quality_id.id else None, line_lst))
    #                     if line_exist:
    #                         item.credit = line_exist[0]['price'] * line_exist[0]['quantity']
    #                         item.debit = line_exist[0]['price'] * line_exist[0]['quantity'] if 'Receivable from Customers' in item.account_id.name else 0.0
    #
    #         else:
    #             line_lst.append({
    #                 'product_id': line.product_id.id,
    #                 'design_id': line.product_id.categ_id.id,
    #                 'quality_id': line.quality_id.id,
    #                 'price': line.price_unit,
    #                 'quantity': line.quantity,
    #                 'price_subtotal': line.price_subtotal,
    #             })
    #
    #             for item in self.line_ids:
    #                 if line.product_id.id == item.product_id.id:
    #                     item.credit = line.price_subtotal
    #                     item.debit = line.price_subtotal if 'Receivable from Customers' in item.account_id.name else 0.0
    #
    #             total_amount += line.price_subtotal
    #
    #     for move in self:
    #         if move.payment_state == 'invoicing_legacy':
    #             # invoicing_legacy state is set via SQL when setting setting field
    #             # invoicing_switch_threshold (defined in account_accountant).
    #             # The only way of going out of this state is through this setting,
    #             # so we don't recompute it here.
    #             move.payment_state = move.payment_state
    #             continue
    #
    #         total_untaxed = 0.0
    #         total_untaxed_currency = 0.0
    #         total_tax = 0.0
    #         total_tax_currency = 0.0
    #         total_to_pay = 0.0
    #         total_residual = 0.0
    #         total_residual_currency = 0.0
    #         total = 0.0
    #         total_currency = 0.0
    #         currencies = move._get_lines_onchange_currency().currency_id
    #
    #         for line in move.line_ids:
    #             if move._payment_state_matters():
    #                 # === Invoices ===
    #
    #                 if not line.exclude_from_invoice_tab:
    #                     # Untaxed amount.
    #                     total_untaxed += line.balance
    #                     total_untaxed_currency += line.amount_currency
    #                     total += line.balance
    #                     total_currency += line.amount_currency
    #                 elif line.tax_line_id:
    #                     # Tax amount.
    #                     total_tax += line.balance
    #                     total_tax_currency += line.amount_currency
    #                     total += line.balance
    #                     total_currency += line.amount_currency
    #                 elif line.account_id.user_type_id.type in ('receivable', 'payable'):
    #                     # Residual amount.
    #                     total_to_pay += line.balance
    #                     total_residual += line.amount_residual
    #                     total_residual_currency += line.amount_residual_currency
    #             else:
    #                 # === Miscellaneous journal entry ===
    #                 if line.debit:
    #                     total += line.balance
    #                     total_currency += line.amount_currency
    #
    #         if move.move_type == 'entry' or move.is_outbound():
    #             sign = 1
    #         else:
    #             sign = -1
    #         move.amount_untaxed = sign * (total_untaxed_currency if len(currencies) == 1 else total_untaxed)
    #         move.amount_tax = sign * (total_tax_currency if len(currencies) == 1 else total_tax)
    #         move.amount_total = total_amount
    #         move.amount_residual = -sign * (total_residual_currency if len(currencies) == 1 else total_residual)
    #         move.amount_untaxed_signed = -total_untaxed
    #         move.amount_tax_signed = -total_tax
    #         move.amount_total_signed = abs(total) if move.move_type == 'entry' else -total
    #         move.amount_residual_signed = total_residual
    #         move.amount_total_in_currency_signed = abs(move.amount_total) if move.move_type == 'entry' else -(sign * move.amount_total)
    #
    #         currency = currencies if len(currencies) == 1 else move.company_id.currency_id
    #
    #         # Compute 'payment_state'.
    #         new_pmt_state = 'not_paid' if move.move_type != 'entry' else False
    #
    #         if move._payment_state_matters() and move.state == 'posted':
    #             if currency.is_zero(move.amount_residual):
    #                 reconciled_payments = move._get_reconciled_payments()
    #                 if not reconciled_payments or all(payment.is_matched for payment in reconciled_payments):
    #                     new_pmt_state = 'paid'
    #                 else:
    #                     new_pmt_state = move._get_invoice_in_payment_state()
    #             elif currency.compare_amounts(total_to_pay, total_residual) != 0:
    #                 new_pmt_state = 'partial'
    #
    #         if new_pmt_state == 'paid' and move.move_type in ('in_invoice', 'out_invoice', 'entry'):
    #             reverse_type = move.move_type == 'in_invoice' and 'in_refund' or move.move_type == 'out_invoice' and 'out_refund' or 'entry'
    #             reverse_moves = self.env['account.move'].search([('reversed_entry_id', '=', move.id), ('state', '=', 'posted'), ('move_type', '=', reverse_type)])
    #
    #             # We only set 'reversed' state in cas of 1 to 1 full reconciliation with a reverse entry; otherwise, we use the regular 'paid' state
    #             reverse_moves_full_recs = reverse_moves.mapped('line_ids.full_reconcile_id')
    #             if reverse_moves_full_recs.mapped('reconciled_line_ids.move_id').filtered(lambda x: x not in (reverse_moves + reverse_moves_full_recs.mapped('exchange_move_id'))) == move:
    #                 new_pmt_state = 'reversed'
    #
    #         move.payment_state = new_pmt_state