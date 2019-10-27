# Created by koche at 10/26/2019
Feature: Test for HW5 selection


  Scenario: User can loop through pants colors
    Given Open Amazon product B07BKGC9V3 page
    Then Verify user can select through jean colors

  Scenario: Every item has word Regular
    Given Open Amazon wholefoods wholefoodsdeals page
    Then Verify every item has a word Regular
