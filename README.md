# Chat System

Chat System is a simple messaging application like Slack, Discord, or Teams. Messages are sent to various channels
within a team. Direct messages can be sent as well. The chat system has concept of threading, where you can respond to a
specific message instead of a message to the whole channel. Notifications are sent to users who are mentioned.

## REST1: Basic Resources & Resource Methods

This phase introduced a basic set of API functions to interact with the Chat System database. The implemented API
functions include: 

 - Listing all _members_
 - Listing all _communities_ and their _channels_
 - Listing all _messages_ from a particular _channel_

These are the available endpoints:

 - `/communities` - gets all _community_ data and its _channels_
 - `/channels/{id}` - gets a specific _channel's_ _messages_
 - `/channels` - gets all _channel_ data
 - `/members` - gets all _member_ data

This phase also included unit tests to ensure proper functionality.

## REST2: CRUD & Authentication

This phase introduced more API functions including user authorization and additional ways for members to interact.
Authorization functionality was implemented with the use of session keys.

Additional endpoints include:

- `/signup` - allows a user to sign up for the Chat System
- `/login` - allows an existing `member` to login to the Chat System
- `/logout` - allows a logged in `member` to log out of the Chat System
- `/dms/{username}?limit` - gets all `direct_message` data for a `member`
  - Optional use of the `limit` parameter to return a specific number of messages

All endpoints (besides `/signup` and `/login`) that perform CRUD operations now require a user to be authorized.