Feature: Demo some common test data creation scenarios

  Scenario: I can log in and save the token
    Given I send a login request
  
  @focus
  Scenario: I can send a simple GET request
    Given I send a simple GET request
    Then the response code is "200"

  Scenario: I can send a simple POST request
    Given I send a simple POST request
    Then the response code is "200"

  Scenario: I can send a predifined JSON body with my POST request
    Given I send a predefined JSON body with my POST request
    Then response contains version "1"

  Scenario: I can send a modified JSON body with my POST request
    Given I send a modified JSON body with my POST request
    Then response contains version "2"

  Scenario: I can pass the response of a request to another request
    Given I send a simple GET request
    Then I can pass the response to another request

  @focus
  Scenario Outline: I can send multiple modified payloads in one scenario
    Given I use "demo.json" as payload
    And I replace version with "<version>"
    And I replace name with "<name>"
    And I send the JSON body with my POST request
    Then response contains version "<version>"

    Examples:
      | version | name      |
      | 2       | vegtables |
      | 3       | animals   |
      | 4       | nuts      |