Feature: call stackoverflow api for questions by tags
  Scenario: enter tags for search
    Given a bot and update from server
    When user send /search django python
    Then return question list