Feature: Search functionality
  Scenario: Search for a valid product
    Given I got navigate to home page
    When I enter valid product into the search box field
    And I click on Search button
    Then valid product should get displayed in Search result
  Scenario: Search for a invalid product
    Given I got navigate to home page
    When  I enter invalid product into the search box field
    And I click on search button
    Then Proper message should be displayed in search result
  Scenario: Search without entering any result
    Given I got navigated to the home page
    When I dont enter anything into search box field
    And I click search button
    Then Proper message should be displayed in search result