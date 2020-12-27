# -*- coding: utf-8 -*-

"""
GNU General Public License v3.0 (GPL v3)
Copyright (c) 2020-2020 WardPearce
Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""


from typing import List, Any


class Recurring:
    aggregate_usage: None
    interval: str
    interval_count: int
    usage_type: str

    def __init__(self, aggregate_usage: None, interval: str,
                 interval_count: int, usage_type: str) -> None:
        self.aggregate_usage = aggregate_usage
        self.interval = interval
        self.interval_count = interval_count
        self.usage_type = usage_type


class Price:
    id: str
    object: str
    active: bool
    billing_scheme: str
    created: int
    currency: str
    livemode: bool
    lookup_key: None
    nickname: None
    product: str
    recurring: Recurring
    tiers_mode: None
    transform_quantity: None
    type: str
    unit_amount: int
    unit_amount_decimal: int

    def __init__(self, id: str, object: str, active: bool, billing_scheme: str,
                 created: int, currency: str, livemode: bool, lookup_key: None,
                 nickname: None, product: str,
                 recurring: Recurring, tiers_mode: None,
                 transform_quantity: None, type: str, unit_amount: int,
                 unit_amount_decimal: int) -> None:
        self.id = id
        self.object = object
        self.active = active
        self.billing_scheme = billing_scheme
        self.created = created
        self.currency = currency
        self.livemode = livemode
        self.lookup_key = lookup_key
        self.nickname = nickname
        self.product = product
        self.recurring = recurring
        self.tiers_mode = tiers_mode
        self.transform_quantity = transform_quantity
        self.type = type
        self.unit_amount = unit_amount
        self.unit_amount_decimal = unit_amount_decimal


class Datum:
    id: str
    object: str
    billing_thresholds: None
    created: int
    price: Price
    quantity: int
    subscription: str
    tax_rates: List[Any]

    def __init__(self, id: str, object: str, billing_thresholds: None,
                 created: int, price: Price,
                 quantity: int, subscription: str,
                 tax_rates: List[Any]) -> None:
        self.id = id
        self.object = object
        self.billing_thresholds = billing_thresholds
        self.created = created
        self.price = price
        self.quantity = quantity
        self.subscription = subscription
        self.tax_rates = tax_rates


class Items:
    object: str
    data: List[Datum]
    has_more: bool
    url: str

    def __init__(self, object: str, data: List[Datum], has_more: bool,
                 url: str) -> None:
        self.object = object
        self.data = data
        self.has_more = has_more
        self.url = url


class Subscription:
    id: str
    object: str
    application_fee_percent: None
    billing_cycle_anchor: int
    billing_thresholds: None
    cancel_at: None
    cancel_at_period_end: bool
    canceled_at: None
    collection_method: str
    created: int
    current_period_end: int
    current_period_start: int
    customer: str
    days_until_due: None
    default_payment_method: None
    default_source: None
    default_tax_rates: List[Any]
    discount: None
    ended_at: None
    items: Items
    latest_invoice: None
    livemode: bool
    next_pending_invoice_item_invoice: None
    pause_collection: None
    pending_invoice_item_interval: None
    pending_setup_intent: None
    pending_update: None
    schedule: None
    start_date: int
    status: str
    transfer_data: None
    trial_end: None
    trial_start: None

    def __init__(self, id: str, object: str, application_fee_percent: None,
                 billing_cycle_anchor: int, billing_thresholds: None,
                 cancel_at: None, cancel_at_period_end: bool,
                 canceled_at: None, collection_method: str,
                 created: int, current_period_end: int,
                 current_period_start: int, customer: str,
                 days_until_due: None, default_payment_method: None,
                 default_source: None, default_tax_rates: List[Any],
                 discount: None, ended_at: None, items: Items,
                 latest_invoice: None,
                 livemode: bool,
                 next_pending_invoice_item_invoice: None,
                 pause_collection: None, pending_invoice_item_interval: None,
                 pending_setup_intent: None, pending_update: None,
                 schedule: None, start_date: int, status: str,
                 transfer_data: None, trial_end: None,
                 trial_start: None) -> None:
        self.id = id
        self.object = object
        self.application_fee_percent = application_fee_percent
        self.billing_cycle_anchor = billing_cycle_anchor
        self.billing_thresholds = billing_thresholds
        self.cancel_at = cancel_at
        self.cancel_at_period_end = cancel_at_period_end
        self.canceled_at = canceled_at
        self.collection_method = collection_method
        self.created = created
        self.current_period_end = current_period_end
        self.current_period_start = current_period_start
        self.customer = customer
        self.days_until_due = days_until_due
        self.default_payment_method = default_payment_method
        self.default_source = default_source
        self.default_tax_rates = default_tax_rates
        self.discount = discount
        self.ended_at = ended_at
        self.items = items
        self.latest_invoice = latest_invoice
        self.livemode = livemode
        self.next_pending_invoice_item_invoice = \
            next_pending_invoice_item_invoice
        self.pause_collection = pause_collection
        self.pending_invoice_item_interval = pending_invoice_item_interval
        self.pending_setup_intent = pending_setup_intent
        self.pending_update = pending_update
        self.schedule = schedule
        self.start_date = start_date
        self.status = status
        self.transfer_data = transfer_data
        self.trial_end = trial_end
        self.trial_start = trial_start
