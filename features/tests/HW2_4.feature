# Created by koche at 10/17/2019
Feature: Test Scenarios for Orders functionality

  Scenario: Logged out user sees Sign in page when clicking orders
    Given Open Amazon home page
    When Click orders link
    Then Verify Sign In page is opened