Feature: Login Functionality
  @completed
  Scenario: Login with valid credentials
    Given I navigate to the login page
    When I enter valid email address and valid password into the field
    And I click on Login Button
    Then I should logged in
  @completed
  Scenario: Login with invalid email and valid password
    Given I navigate to the login page
    When I enter invalid email and valid password into the field
    And I click on Login Button
    Then I should get a proper warning message
  @completed
  Scenario: Login with valid email and invalid password
    Given I navigate to the login page
    When I enter valid email and invalid password into the field
    And I click on Login Button
    Then I should get a proper warning message
  @completed
  Scenario: Login with invalid credentials
    Given I navigate to the login page
    When I enter invalid email and invalid password into the field
    And I click on Login Button
    Then I should get a proper warning message
  @completed
  Scenario: Login without entering any credentials
    Given I navigate to the login page
    When I dont enter anything into the email and password fields
    And  I click on login button
    Then I should get a proper warning message
