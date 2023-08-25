Commit 1: Initial Setup

     Created a new Django project and app for asset tracking.
     Configured database settings and installed necessary packages.

Commit 2: Model Setup

    Added models for Company, Employee, DeviceType, Device, and DeviceLog.
    Defined relationships between models and set up database schema.

Commit 3: Serializer,views,urls Setup

    Created serializers for Company, Employee, DeviceType, Device, and DeviceLog.
    Used nested serializers for related models.
    Created viewsets for Company, Employee, DeviceType, Device, and DeviceLog.
    Configured URLs for the viewsets in the app's urls.py.

Commit 5: Permissions and Authentication

    Added permission classes to restrict access to authenticated users.
    Set up token-based authentication for API endpoints.

Commit 6: Tests for Models and Views

    Added test cases for models and viewset methods.
    Covered scenarios like creating instances and retrieving data.

Commit 7: Automated API Documentation

    Integrated DRF YASG for automatic API documentation.
    Updated URLs to include a /swagger/ endpoint.


Commit 8: Custom Validation

    Added custom validation methods in serializers.
    Validated fields like return_date in DeviceLog serializer.

Commit 11: Placeholder Code for Payments

   Added placeholder code for integrating payments or subscriptions.
   Demonstrated the structure for payment-related functionality.

Commit 12: Code Cleanup and Finalization

   Reviewed code, removed redundant sections, and improved comments.
   Ensured consistent code style and readability.