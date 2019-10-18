# Created by koche at 10/17/2019
Feature: Test Scenarios for Cancel Order help search
  #user enters 'cancel order' in help search and get results for 'cancel order' input

  Scenario: User can search in help section
    Given Open Amazon home page
    When Click Help link
    And Type in Cancel Order
    Then Verify cancel order is displayed

