Feature: Tiendeo landing page

  Scenario: landing page loads OK
    Given valid url address
    when navigate to the url on a browser
    then should load the webpage

  Scenario: location is selectable
    Given a valid location
    when select location using form
    then should show location information
    and should show location information navbar
    and should show location description

  Scenario: landing page well formated
    Given a correct webpage
    when navigating on webpage
    then should exist category navigation bar
    and should exist top offer section
    and should exist top stores
    and should exist suscribe alert
    and should exist top categories
    and should exist starred products
    and should exist comercial shop center list
    and should exist location information
    and should exist tiendeo information
    and should exist tiendeo international links
    and should exist tiendeo mobile app

  Scenario: search form
    Given a valid product
    when search for a product
    then offers should be related to this product