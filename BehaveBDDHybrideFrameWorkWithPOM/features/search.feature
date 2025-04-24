Feature: Search functionality
  @search
  Scenario: Search for a valid product
    Given I got navigate to the home page
    When I enter valid product into the search box field
    And I click on search button
    Then valid product should get displayed in Search results
  @search
  Scenario: Search for a invalid product
    Given I got navigate to the home page
    When I enter invalid product into the search box field
    And I click on search button
    Then Proper Message should be displayed in Search result
  @search
  Scenario:  Search without Entering any product
    Given I got navigate to the home page
    When I dont enter anything into the Search box filed
    And I click on Search button
    Then Proper Message should be displayed in Search result
