Feature: Register Account functionality
  Scenario: Register with mandatory fields
    Given I navigate to Register Page
    When I enter mandatory fields
    And I click on Continue button
    Then Account should be created

  Scenario: Register with all fields
    Given I navigate to Register page
    When I enter all fields
    And I click on continue button
    Then Account should be created

  Scenario: Register with a duplicate email address
    Given I navigate to register page
    When I enter details into all fields except email field
    And I enter existing account email into email field
    And I click on continue button
    Then Proper warning message informing about duplicate account should be displayed

  Scenario: Register without providing any details
    Given I navigate to Register page
    When I dont enter anything into the field
    And I click on continue button
    Then Proper warning message for every mandatory fields should be displayed
