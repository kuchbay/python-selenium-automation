# Created by koche at 11/1/2019
Feature: HW6
  # Enter feature description here

  Scenario: User can open and close Today's deals under 25
    Given Open Amazon page
    When Store original windows
    And Click to open Deals under 25
    And Switch to the newly opened window
    Then Shop all deals is shown
    When Click to add a product from deals to cart
    When And User can close new window and switch back to original
    When Refresh the page
    Then Verify cart has 1 item
