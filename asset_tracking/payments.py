import stripe

stripe.api_key = 'stripe_api_key'

def create_subscription(customer_id, plan_id):
    subscription = stripe.Subscription.create(
        customer=customer_id,
        items=[{'price': plan_id}],
    )
    return subscription