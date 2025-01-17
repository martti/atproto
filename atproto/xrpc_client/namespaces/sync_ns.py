##################################################################
# THIS IS THE AUTO-GENERATED CODE. DON'T EDIT IT BY HANDS!
# Copyright (C) 2023 Ilya (Marshal) <https://github.com/MarshalX>.
# This file is part of Python atproto SDK. Licenced under MIT.
##################################################################


import typing as t

from atproto.xrpc_client import models
from atproto.xrpc_client.models.utils import get_or_create, get_response_model
from atproto.xrpc_client.namespaces.base import NamespaceBase

if t.TYPE_CHECKING:
    from atproto.xrpc_client.client.raw import ClientRaw


class AppNamespace(NamespaceBase):
    def __init__(self, client: 'ClientRaw') -> None:
        super().__init__(client)
        self.bsky = BskyNamespace(self._client)


class BskyNamespace(NamespaceBase):
    def __init__(self, client: 'ClientRaw') -> None:
        super().__init__(client)
        self.actor = ActorNamespace(self._client)
        self.feed = FeedNamespace(self._client)
        self.graph = GraphNamespace(self._client)
        self.notification = NotificationNamespace(self._client)
        self.unspecced = UnspeccedNamespace(self._client)


class ActorNamespace(NamespaceBase):
    def get_preferences(
        self,
        params: t.Optional[
            t.Union[models.AppBskyActorGetPreferences.Params, models.AppBskyActorGetPreferences.ParamsDict]
        ] = None,
        **kwargs: t.Any,
    ) -> 'models.AppBskyActorGetPreferences.Response':
        """Get private preferences attached to the account.

        Args:
            params: Parameters.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.AppBskyActorGetPreferences.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        params_model = get_or_create(params, models.AppBskyActorGetPreferences.Params)
        response = self._client.invoke_query(
            'app.bsky.actor.getPreferences', params=params_model, output_encoding='application/json', **kwargs
        )
        return get_response_model(response, models.AppBskyActorGetPreferences.Response)

    def get_profile(
        self,
        params: t.Union[models.AppBskyActorGetProfile.Params, models.AppBskyActorGetProfile.ParamsDict],
        **kwargs: t.Any,
    ) -> 'models.AppBskyActorDefs.ProfileViewDetailed':
        """Get profile.

        Args:
            params: Parameters.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.AppBskyActorDefs.ProfileViewDetailed`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        params_model = get_or_create(params, models.AppBskyActorGetProfile.Params)
        response = self._client.invoke_query(
            'app.bsky.actor.getProfile', params=params_model, output_encoding='application/json', **kwargs
        )
        return get_response_model(response, models.AppBskyActorDefs.ProfileViewDetailed)

    def get_profiles(
        self,
        params: t.Union[models.AppBskyActorGetProfiles.Params, models.AppBskyActorGetProfiles.ParamsDict],
        **kwargs: t.Any,
    ) -> 'models.AppBskyActorGetProfiles.Response':
        """Get profiles.

        Args:
            params: Parameters.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.AppBskyActorGetProfiles.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        params_model = get_or_create(params, models.AppBskyActorGetProfiles.Params)
        response = self._client.invoke_query(
            'app.bsky.actor.getProfiles', params=params_model, output_encoding='application/json', **kwargs
        )
        return get_response_model(response, models.AppBskyActorGetProfiles.Response)

    def get_suggestions(
        self,
        params: t.Optional[
            t.Union[models.AppBskyActorGetSuggestions.Params, models.AppBskyActorGetSuggestions.ParamsDict]
        ] = None,
        **kwargs: t.Any,
    ) -> 'models.AppBskyActorGetSuggestions.Response':
        """Get a list of actors suggested for following. Used in discovery UIs.

        Args:
            params: Parameters.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.AppBskyActorGetSuggestions.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        params_model = get_or_create(params, models.AppBskyActorGetSuggestions.Params)
        response = self._client.invoke_query(
            'app.bsky.actor.getSuggestions', params=params_model, output_encoding='application/json', **kwargs
        )
        return get_response_model(response, models.AppBskyActorGetSuggestions.Response)

    def put_preferences(
        self,
        data: t.Union[models.AppBskyActorPutPreferences.Data, models.AppBskyActorPutPreferences.DataDict],
        **kwargs: t.Any,
    ) -> bool:
        """Sets the private preferences attached to the account.

        Args:
            data: Input data.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`bool`: Success status.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        data_model = get_or_create(data, models.AppBskyActorPutPreferences.Data)
        response = self._client.invoke_procedure(
            'app.bsky.actor.putPreferences', data=data_model, input_encoding='application/json', **kwargs
        )
        return get_response_model(response, bool)

    def search_actors(
        self,
        params: t.Optional[
            t.Union[models.AppBskyActorSearchActors.Params, models.AppBskyActorSearchActors.ParamsDict]
        ] = None,
        **kwargs: t.Any,
    ) -> 'models.AppBskyActorSearchActors.Response':
        """Find actors (profiles) matching search criteria.

        Args:
            params: Parameters.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.AppBskyActorSearchActors.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        params_model = get_or_create(params, models.AppBskyActorSearchActors.Params)
        response = self._client.invoke_query(
            'app.bsky.actor.searchActors', params=params_model, output_encoding='application/json', **kwargs
        )
        return get_response_model(response, models.AppBskyActorSearchActors.Response)

    def search_actors_typeahead(
        self,
        params: t.Optional[
            t.Union[
                models.AppBskyActorSearchActorsTypeahead.Params, models.AppBskyActorSearchActorsTypeahead.ParamsDict
            ]
        ] = None,
        **kwargs: t.Any,
    ) -> 'models.AppBskyActorSearchActorsTypeahead.Response':
        """Find actor suggestions for a search term.

        Args:
            params: Parameters.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.AppBskyActorSearchActorsTypeahead.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        params_model = get_or_create(params, models.AppBskyActorSearchActorsTypeahead.Params)
        response = self._client.invoke_query(
            'app.bsky.actor.searchActorsTypeahead', params=params_model, output_encoding='application/json', **kwargs
        )
        return get_response_model(response, models.AppBskyActorSearchActorsTypeahead.Response)


class FeedNamespace(NamespaceBase):
    def describe_feed_generator(self, **kwargs: t.Any) -> 'models.AppBskyFeedDescribeFeedGenerator.Response':
        """Returns information about a given feed generator including TOS & offered feed URIs.

        Args:
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.AppBskyFeedDescribeFeedGenerator.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        response = self._client.invoke_query(
            'app.bsky.feed.describeFeedGenerator', output_encoding='application/json', **kwargs
        )
        return get_response_model(response, models.AppBskyFeedDescribeFeedGenerator.Response)

    def get_actor_feeds(
        self,
        params: t.Union[models.AppBskyFeedGetActorFeeds.Params, models.AppBskyFeedGetActorFeeds.ParamsDict],
        **kwargs: t.Any,
    ) -> 'models.AppBskyFeedGetActorFeeds.Response':
        """Retrieve a list of feeds created by a given actor.

        Args:
            params: Parameters.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.AppBskyFeedGetActorFeeds.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        params_model = get_or_create(params, models.AppBskyFeedGetActorFeeds.Params)
        response = self._client.invoke_query(
            'app.bsky.feed.getActorFeeds', params=params_model, output_encoding='application/json', **kwargs
        )
        return get_response_model(response, models.AppBskyFeedGetActorFeeds.Response)

    def get_actor_likes(
        self,
        params: t.Union[models.AppBskyFeedGetActorLikes.Params, models.AppBskyFeedGetActorLikes.ParamsDict],
        **kwargs: t.Any,
    ) -> 'models.AppBskyFeedGetActorLikes.Response':
        """A view of the posts liked by an actor.

        Args:
            params: Parameters.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.AppBskyFeedGetActorLikes.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        params_model = get_or_create(params, models.AppBskyFeedGetActorLikes.Params)
        response = self._client.invoke_query(
            'app.bsky.feed.getActorLikes', params=params_model, output_encoding='application/json', **kwargs
        )
        return get_response_model(response, models.AppBskyFeedGetActorLikes.Response)

    def get_author_feed(
        self,
        params: t.Union[models.AppBskyFeedGetAuthorFeed.Params, models.AppBskyFeedGetAuthorFeed.ParamsDict],
        **kwargs: t.Any,
    ) -> 'models.AppBskyFeedGetAuthorFeed.Response':
        """A view of an actor's feed.

        Args:
            params: Parameters.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.AppBskyFeedGetAuthorFeed.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        params_model = get_or_create(params, models.AppBskyFeedGetAuthorFeed.Params)
        response = self._client.invoke_query(
            'app.bsky.feed.getAuthorFeed', params=params_model, output_encoding='application/json', **kwargs
        )
        return get_response_model(response, models.AppBskyFeedGetAuthorFeed.Response)

    def get_feed(
        self, params: t.Union[models.AppBskyFeedGetFeed.Params, models.AppBskyFeedGetFeed.ParamsDict], **kwargs: t.Any
    ) -> 'models.AppBskyFeedGetFeed.Response':
        """Compose and hydrate a feed from a user's selected feed generator.

        Args:
            params: Parameters.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.AppBskyFeedGetFeed.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        params_model = get_or_create(params, models.AppBskyFeedGetFeed.Params)
        response = self._client.invoke_query(
            'app.bsky.feed.getFeed', params=params_model, output_encoding='application/json', **kwargs
        )
        return get_response_model(response, models.AppBskyFeedGetFeed.Response)

    def get_feed_generator(
        self,
        params: t.Union[models.AppBskyFeedGetFeedGenerator.Params, models.AppBskyFeedGetFeedGenerator.ParamsDict],
        **kwargs: t.Any,
    ) -> 'models.AppBskyFeedGetFeedGenerator.Response':
        """Get information about a specific feed offered by a feed generator, such as its online status.

        Args:
            params: Parameters.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.AppBskyFeedGetFeedGenerator.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        params_model = get_or_create(params, models.AppBskyFeedGetFeedGenerator.Params)
        response = self._client.invoke_query(
            'app.bsky.feed.getFeedGenerator', params=params_model, output_encoding='application/json', **kwargs
        )
        return get_response_model(response, models.AppBskyFeedGetFeedGenerator.Response)

    def get_feed_generators(
        self,
        params: t.Union[models.AppBskyFeedGetFeedGenerators.Params, models.AppBskyFeedGetFeedGenerators.ParamsDict],
        **kwargs: t.Any,
    ) -> 'models.AppBskyFeedGetFeedGenerators.Response':
        """Get information about a list of feed generators.

        Args:
            params: Parameters.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.AppBskyFeedGetFeedGenerators.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        params_model = get_or_create(params, models.AppBskyFeedGetFeedGenerators.Params)
        response = self._client.invoke_query(
            'app.bsky.feed.getFeedGenerators', params=params_model, output_encoding='application/json', **kwargs
        )
        return get_response_model(response, models.AppBskyFeedGetFeedGenerators.Response)

    def get_feed_skeleton(
        self,
        params: t.Union[models.AppBskyFeedGetFeedSkeleton.Params, models.AppBskyFeedGetFeedSkeleton.ParamsDict],
        **kwargs: t.Any,
    ) -> 'models.AppBskyFeedGetFeedSkeleton.Response':
        """A skeleton of a feed provided by a feed generator.

        Args:
            params: Parameters.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.AppBskyFeedGetFeedSkeleton.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        params_model = get_or_create(params, models.AppBskyFeedGetFeedSkeleton.Params)
        response = self._client.invoke_query(
            'app.bsky.feed.getFeedSkeleton', params=params_model, output_encoding='application/json', **kwargs
        )
        return get_response_model(response, models.AppBskyFeedGetFeedSkeleton.Response)

    def get_likes(
        self, params: t.Union[models.AppBskyFeedGetLikes.Params, models.AppBskyFeedGetLikes.ParamsDict], **kwargs: t.Any
    ) -> 'models.AppBskyFeedGetLikes.Response':
        """Get likes.

        Args:
            params: Parameters.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.AppBskyFeedGetLikes.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        params_model = get_or_create(params, models.AppBskyFeedGetLikes.Params)
        response = self._client.invoke_query(
            'app.bsky.feed.getLikes', params=params_model, output_encoding='application/json', **kwargs
        )
        return get_response_model(response, models.AppBskyFeedGetLikes.Response)

    def get_list_feed(
        self,
        params: t.Union[models.AppBskyFeedGetListFeed.Params, models.AppBskyFeedGetListFeed.ParamsDict],
        **kwargs: t.Any,
    ) -> 'models.AppBskyFeedGetListFeed.Response':
        """A view of a recent posts from actors in a list.

        Args:
            params: Parameters.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.AppBskyFeedGetListFeed.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        params_model = get_or_create(params, models.AppBskyFeedGetListFeed.Params)
        response = self._client.invoke_query(
            'app.bsky.feed.getListFeed', params=params_model, output_encoding='application/json', **kwargs
        )
        return get_response_model(response, models.AppBskyFeedGetListFeed.Response)

    def get_post_thread(
        self,
        params: t.Union[models.AppBskyFeedGetPostThread.Params, models.AppBskyFeedGetPostThread.ParamsDict],
        **kwargs: t.Any,
    ) -> 'models.AppBskyFeedGetPostThread.Response':
        """Get post thread.

        Args:
            params: Parameters.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.AppBskyFeedGetPostThread.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        params_model = get_or_create(params, models.AppBskyFeedGetPostThread.Params)
        response = self._client.invoke_query(
            'app.bsky.feed.getPostThread', params=params_model, output_encoding='application/json', **kwargs
        )
        return get_response_model(response, models.AppBskyFeedGetPostThread.Response)

    def get_posts(
        self, params: t.Union[models.AppBskyFeedGetPosts.Params, models.AppBskyFeedGetPosts.ParamsDict], **kwargs: t.Any
    ) -> 'models.AppBskyFeedGetPosts.Response':
        """A view of an actor's feed.

        Args:
            params: Parameters.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.AppBskyFeedGetPosts.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        params_model = get_or_create(params, models.AppBskyFeedGetPosts.Params)
        response = self._client.invoke_query(
            'app.bsky.feed.getPosts', params=params_model, output_encoding='application/json', **kwargs
        )
        return get_response_model(response, models.AppBskyFeedGetPosts.Response)

    def get_reposted_by(
        self,
        params: t.Union[models.AppBskyFeedGetRepostedBy.Params, models.AppBskyFeedGetRepostedBy.ParamsDict],
        **kwargs: t.Any,
    ) -> 'models.AppBskyFeedGetRepostedBy.Response':
        """Get reposted by.

        Args:
            params: Parameters.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.AppBskyFeedGetRepostedBy.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        params_model = get_or_create(params, models.AppBskyFeedGetRepostedBy.Params)
        response = self._client.invoke_query(
            'app.bsky.feed.getRepostedBy', params=params_model, output_encoding='application/json', **kwargs
        )
        return get_response_model(response, models.AppBskyFeedGetRepostedBy.Response)

    def get_suggested_feeds(
        self,
        params: t.Optional[
            t.Union[models.AppBskyFeedGetSuggestedFeeds.Params, models.AppBskyFeedGetSuggestedFeeds.ParamsDict]
        ] = None,
        **kwargs: t.Any,
    ) -> 'models.AppBskyFeedGetSuggestedFeeds.Response':
        """Get a list of suggested feeds for the viewer.

        Args:
            params: Parameters.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.AppBskyFeedGetSuggestedFeeds.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        params_model = get_or_create(params, models.AppBskyFeedGetSuggestedFeeds.Params)
        response = self._client.invoke_query(
            'app.bsky.feed.getSuggestedFeeds', params=params_model, output_encoding='application/json', **kwargs
        )
        return get_response_model(response, models.AppBskyFeedGetSuggestedFeeds.Response)

    def get_timeline(
        self,
        params: t.Optional[
            t.Union[models.AppBskyFeedGetTimeline.Params, models.AppBskyFeedGetTimeline.ParamsDict]
        ] = None,
        **kwargs: t.Any,
    ) -> 'models.AppBskyFeedGetTimeline.Response':
        """A view of the user's home timeline.

        Args:
            params: Parameters.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.AppBskyFeedGetTimeline.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        params_model = get_or_create(params, models.AppBskyFeedGetTimeline.Params)
        response = self._client.invoke_query(
            'app.bsky.feed.getTimeline', params=params_model, output_encoding='application/json', **kwargs
        )
        return get_response_model(response, models.AppBskyFeedGetTimeline.Response)

    def search_posts(
        self,
        params: t.Union[models.AppBskyFeedSearchPosts.Params, models.AppBskyFeedSearchPosts.ParamsDict],
        **kwargs: t.Any,
    ) -> 'models.AppBskyFeedSearchPosts.Response':
        """Find posts matching search criteria.

        Args:
            params: Parameters.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.AppBskyFeedSearchPosts.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        params_model = get_or_create(params, models.AppBskyFeedSearchPosts.Params)
        response = self._client.invoke_query(
            'app.bsky.feed.searchPosts', params=params_model, output_encoding='application/json', **kwargs
        )
        return get_response_model(response, models.AppBskyFeedSearchPosts.Response)


class GraphNamespace(NamespaceBase):
    def get_blocks(
        self,
        params: t.Optional[
            t.Union[models.AppBskyGraphGetBlocks.Params, models.AppBskyGraphGetBlocks.ParamsDict]
        ] = None,
        **kwargs: t.Any,
    ) -> 'models.AppBskyGraphGetBlocks.Response':
        """Who is the requester's account blocking?

        Args:
            params: Parameters.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.AppBskyGraphGetBlocks.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        params_model = get_or_create(params, models.AppBskyGraphGetBlocks.Params)
        response = self._client.invoke_query(
            'app.bsky.graph.getBlocks', params=params_model, output_encoding='application/json', **kwargs
        )
        return get_response_model(response, models.AppBskyGraphGetBlocks.Response)

    def get_followers(
        self,
        params: t.Union[models.AppBskyGraphGetFollowers.Params, models.AppBskyGraphGetFollowers.ParamsDict],
        **kwargs: t.Any,
    ) -> 'models.AppBskyGraphGetFollowers.Response':
        """Who is following an actor?

        Args:
            params: Parameters.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.AppBskyGraphGetFollowers.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        params_model = get_or_create(params, models.AppBskyGraphGetFollowers.Params)
        response = self._client.invoke_query(
            'app.bsky.graph.getFollowers', params=params_model, output_encoding='application/json', **kwargs
        )
        return get_response_model(response, models.AppBskyGraphGetFollowers.Response)

    def get_follows(
        self,
        params: t.Union[models.AppBskyGraphGetFollows.Params, models.AppBskyGraphGetFollows.ParamsDict],
        **kwargs: t.Any,
    ) -> 'models.AppBskyGraphGetFollows.Response':
        """Who is an actor following?

        Args:
            params: Parameters.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.AppBskyGraphGetFollows.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        params_model = get_or_create(params, models.AppBskyGraphGetFollows.Params)
        response = self._client.invoke_query(
            'app.bsky.graph.getFollows', params=params_model, output_encoding='application/json', **kwargs
        )
        return get_response_model(response, models.AppBskyGraphGetFollows.Response)

    def get_list(
        self, params: t.Union[models.AppBskyGraphGetList.Params, models.AppBskyGraphGetList.ParamsDict], **kwargs: t.Any
    ) -> 'models.AppBskyGraphGetList.Response':
        """Fetch a list of actors.

        Args:
            params: Parameters.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.AppBskyGraphGetList.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        params_model = get_or_create(params, models.AppBskyGraphGetList.Params)
        response = self._client.invoke_query(
            'app.bsky.graph.getList', params=params_model, output_encoding='application/json', **kwargs
        )
        return get_response_model(response, models.AppBskyGraphGetList.Response)

    def get_list_blocks(
        self,
        params: t.Optional[
            t.Union[models.AppBskyGraphGetListBlocks.Params, models.AppBskyGraphGetListBlocks.ParamsDict]
        ] = None,
        **kwargs: t.Any,
    ) -> 'models.AppBskyGraphGetListBlocks.Response':
        """Which lists is the requester's account blocking?

        Args:
            params: Parameters.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.AppBskyGraphGetListBlocks.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        params_model = get_or_create(params, models.AppBskyGraphGetListBlocks.Params)
        response = self._client.invoke_query(
            'app.bsky.graph.getListBlocks', params=params_model, output_encoding='application/json', **kwargs
        )
        return get_response_model(response, models.AppBskyGraphGetListBlocks.Response)

    def get_list_mutes(
        self,
        params: t.Optional[
            t.Union[models.AppBskyGraphGetListMutes.Params, models.AppBskyGraphGetListMutes.ParamsDict]
        ] = None,
        **kwargs: t.Any,
    ) -> 'models.AppBskyGraphGetListMutes.Response':
        """Which lists is the requester's account muting?

        Args:
            params: Parameters.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.AppBskyGraphGetListMutes.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        params_model = get_or_create(params, models.AppBskyGraphGetListMutes.Params)
        response = self._client.invoke_query(
            'app.bsky.graph.getListMutes', params=params_model, output_encoding='application/json', **kwargs
        )
        return get_response_model(response, models.AppBskyGraphGetListMutes.Response)

    def get_lists(
        self,
        params: t.Union[models.AppBskyGraphGetLists.Params, models.AppBskyGraphGetLists.ParamsDict],
        **kwargs: t.Any,
    ) -> 'models.AppBskyGraphGetLists.Response':
        """Fetch a list of lists that belong to an actor.

        Args:
            params: Parameters.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.AppBskyGraphGetLists.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        params_model = get_or_create(params, models.AppBskyGraphGetLists.Params)
        response = self._client.invoke_query(
            'app.bsky.graph.getLists', params=params_model, output_encoding='application/json', **kwargs
        )
        return get_response_model(response, models.AppBskyGraphGetLists.Response)

    def get_mutes(
        self,
        params: t.Optional[t.Union[models.AppBskyGraphGetMutes.Params, models.AppBskyGraphGetMutes.ParamsDict]] = None,
        **kwargs: t.Any,
    ) -> 'models.AppBskyGraphGetMutes.Response':
        """Who does the viewer mute?

        Args:
            params: Parameters.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.AppBskyGraphGetMutes.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        params_model = get_or_create(params, models.AppBskyGraphGetMutes.Params)
        response = self._client.invoke_query(
            'app.bsky.graph.getMutes', params=params_model, output_encoding='application/json', **kwargs
        )
        return get_response_model(response, models.AppBskyGraphGetMutes.Response)

    def get_suggested_follows_by_actor(
        self,
        params: t.Union[
            models.AppBskyGraphGetSuggestedFollowsByActor.Params,
            models.AppBskyGraphGetSuggestedFollowsByActor.ParamsDict,
        ],
        **kwargs: t.Any,
    ) -> 'models.AppBskyGraphGetSuggestedFollowsByActor.Response':
        """Get suggested follows related to a given actor.

        Args:
            params: Parameters.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.AppBskyGraphGetSuggestedFollowsByActor.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        params_model = get_or_create(params, models.AppBskyGraphGetSuggestedFollowsByActor.Params)
        response = self._client.invoke_query(
            'app.bsky.graph.getSuggestedFollowsByActor',
            params=params_model,
            output_encoding='application/json',
            **kwargs,
        )
        return get_response_model(response, models.AppBskyGraphGetSuggestedFollowsByActor.Response)

    def mute_actor(
        self, data: t.Union[models.AppBskyGraphMuteActor.Data, models.AppBskyGraphMuteActor.DataDict], **kwargs: t.Any
    ) -> bool:
        """Mute an actor by did or handle.

        Args:
            data: Input data.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`bool`: Success status.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        data_model = get_or_create(data, models.AppBskyGraphMuteActor.Data)
        response = self._client.invoke_procedure(
            'app.bsky.graph.muteActor', data=data_model, input_encoding='application/json', **kwargs
        )
        return get_response_model(response, bool)

    def mute_actor_list(
        self,
        data: t.Union[models.AppBskyGraphMuteActorList.Data, models.AppBskyGraphMuteActorList.DataDict],
        **kwargs: t.Any,
    ) -> bool:
        """Mute a list of actors.

        Args:
            data: Input data.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`bool`: Success status.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        data_model = get_or_create(data, models.AppBskyGraphMuteActorList.Data)
        response = self._client.invoke_procedure(
            'app.bsky.graph.muteActorList', data=data_model, input_encoding='application/json', **kwargs
        )
        return get_response_model(response, bool)

    def unmute_actor(
        self,
        data: t.Union[models.AppBskyGraphUnmuteActor.Data, models.AppBskyGraphUnmuteActor.DataDict],
        **kwargs: t.Any,
    ) -> bool:
        """Unmute an actor by did or handle.

        Args:
            data: Input data.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`bool`: Success status.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        data_model = get_or_create(data, models.AppBskyGraphUnmuteActor.Data)
        response = self._client.invoke_procedure(
            'app.bsky.graph.unmuteActor', data=data_model, input_encoding='application/json', **kwargs
        )
        return get_response_model(response, bool)

    def unmute_actor_list(
        self,
        data: t.Union[models.AppBskyGraphUnmuteActorList.Data, models.AppBskyGraphUnmuteActorList.DataDict],
        **kwargs: t.Any,
    ) -> bool:
        """Unmute a list of actors.

        Args:
            data: Input data.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`bool`: Success status.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        data_model = get_or_create(data, models.AppBskyGraphUnmuteActorList.Data)
        response = self._client.invoke_procedure(
            'app.bsky.graph.unmuteActorList', data=data_model, input_encoding='application/json', **kwargs
        )
        return get_response_model(response, bool)


class NotificationNamespace(NamespaceBase):
    def get_unread_count(
        self,
        params: t.Optional[
            t.Union[
                models.AppBskyNotificationGetUnreadCount.Params, models.AppBskyNotificationGetUnreadCount.ParamsDict
            ]
        ] = None,
        **kwargs: t.Any,
    ) -> 'models.AppBskyNotificationGetUnreadCount.Response':
        """Get unread count.

        Args:
            params: Parameters.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.AppBskyNotificationGetUnreadCount.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        params_model = get_or_create(params, models.AppBskyNotificationGetUnreadCount.Params)
        response = self._client.invoke_query(
            'app.bsky.notification.getUnreadCount', params=params_model, output_encoding='application/json', **kwargs
        )
        return get_response_model(response, models.AppBskyNotificationGetUnreadCount.Response)

    def list_notifications(
        self,
        params: t.Optional[
            t.Union[
                models.AppBskyNotificationListNotifications.Params,
                models.AppBskyNotificationListNotifications.ParamsDict,
            ]
        ] = None,
        **kwargs: t.Any,
    ) -> 'models.AppBskyNotificationListNotifications.Response':
        """List notifications.

        Args:
            params: Parameters.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.AppBskyNotificationListNotifications.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        params_model = get_or_create(params, models.AppBskyNotificationListNotifications.Params)
        response = self._client.invoke_query(
            'app.bsky.notification.listNotifications', params=params_model, output_encoding='application/json', **kwargs
        )
        return get_response_model(response, models.AppBskyNotificationListNotifications.Response)

    def register_push(
        self,
        data: t.Union[models.AppBskyNotificationRegisterPush.Data, models.AppBskyNotificationRegisterPush.DataDict],
        **kwargs: t.Any,
    ) -> bool:
        """Register for push notifications with a service.

        Args:
            data: Input data.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`bool`: Success status.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        data_model = get_or_create(data, models.AppBskyNotificationRegisterPush.Data)
        response = self._client.invoke_procedure(
            'app.bsky.notification.registerPush', data=data_model, input_encoding='application/json', **kwargs
        )
        return get_response_model(response, bool)

    def update_seen(
        self,
        data: t.Union[models.AppBskyNotificationUpdateSeen.Data, models.AppBskyNotificationUpdateSeen.DataDict],
        **kwargs: t.Any,
    ) -> bool:
        """Notify server that the user has seen notifications.

        Args:
            data: Input data.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`bool`: Success status.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        data_model = get_or_create(data, models.AppBskyNotificationUpdateSeen.Data)
        response = self._client.invoke_procedure(
            'app.bsky.notification.updateSeen', data=data_model, input_encoding='application/json', **kwargs
        )
        return get_response_model(response, bool)


class UnspeccedNamespace(NamespaceBase):
    def apply_labels(
        self,
        data: t.Union[models.AppBskyUnspeccedApplyLabels.Data, models.AppBskyUnspeccedApplyLabels.DataDict],
        **kwargs: t.Any,
    ) -> bool:
        """Allow a labeler to apply labels directly.

        Args:
            data: Input data.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`bool`: Success status.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        data_model = get_or_create(data, models.AppBskyUnspeccedApplyLabels.Data)
        response = self._client.invoke_procedure(
            'app.bsky.unspecced.applyLabels', data=data_model, input_encoding='application/json', **kwargs
        )
        return get_response_model(response, bool)

    def get_popular(
        self,
        params: t.Optional[
            t.Union[models.AppBskyUnspeccedGetPopular.Params, models.AppBskyUnspeccedGetPopular.ParamsDict]
        ] = None,
        **kwargs: t.Any,
    ) -> 'models.AppBskyUnspeccedGetPopular.Response':
        """DEPRECATED: will be removed soon, please find a feed generator alternative.

        Args:
            params: Parameters.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.AppBskyUnspeccedGetPopular.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        params_model = get_or_create(params, models.AppBskyUnspeccedGetPopular.Params)
        response = self._client.invoke_query(
            'app.bsky.unspecced.getPopular', params=params_model, output_encoding='application/json', **kwargs
        )
        return get_response_model(response, models.AppBskyUnspeccedGetPopular.Response)

    def get_popular_feed_generators(
        self,
        params: t.Optional[
            t.Union[
                models.AppBskyUnspeccedGetPopularFeedGenerators.Params,
                models.AppBskyUnspeccedGetPopularFeedGenerators.ParamsDict,
            ]
        ] = None,
        **kwargs: t.Any,
    ) -> 'models.AppBskyUnspeccedGetPopularFeedGenerators.Response':
        """An unspecced view of globally popular feed generators.

        Args:
            params: Parameters.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.AppBskyUnspeccedGetPopularFeedGenerators.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        params_model = get_or_create(params, models.AppBskyUnspeccedGetPopularFeedGenerators.Params)
        response = self._client.invoke_query(
            'app.bsky.unspecced.getPopularFeedGenerators',
            params=params_model,
            output_encoding='application/json',
            **kwargs,
        )
        return get_response_model(response, models.AppBskyUnspeccedGetPopularFeedGenerators.Response)

    def get_timeline_skeleton(
        self,
        params: t.Optional[
            t.Union[
                models.AppBskyUnspeccedGetTimelineSkeleton.Params, models.AppBskyUnspeccedGetTimelineSkeleton.ParamsDict
            ]
        ] = None,
        **kwargs: t.Any,
    ) -> 'models.AppBskyUnspeccedGetTimelineSkeleton.Response':
        """A skeleton of a timeline - UNSPECCED & WILL GO AWAY SOON.

        Args:
            params: Parameters.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.AppBskyUnspeccedGetTimelineSkeleton.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        params_model = get_or_create(params, models.AppBskyUnspeccedGetTimelineSkeleton.Params)
        response = self._client.invoke_query(
            'app.bsky.unspecced.getTimelineSkeleton', params=params_model, output_encoding='application/json', **kwargs
        )
        return get_response_model(response, models.AppBskyUnspeccedGetTimelineSkeleton.Response)

    def search_actors_skeleton(
        self,
        params: t.Union[
            models.AppBskyUnspeccedSearchActorsSkeleton.Params, models.AppBskyUnspeccedSearchActorsSkeleton.ParamsDict
        ],
        **kwargs: t.Any,
    ) -> 'models.AppBskyUnspeccedSearchActorsSkeleton.Response':
        """Backend Actors (profile) search, returning only skeleton.

        Args:
            params: Parameters.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.AppBskyUnspeccedSearchActorsSkeleton.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        params_model = get_or_create(params, models.AppBskyUnspeccedSearchActorsSkeleton.Params)
        response = self._client.invoke_query(
            'app.bsky.unspecced.searchActorsSkeleton', params=params_model, output_encoding='application/json', **kwargs
        )
        return get_response_model(response, models.AppBskyUnspeccedSearchActorsSkeleton.Response)

    def search_posts_skeleton(
        self,
        params: t.Union[
            models.AppBskyUnspeccedSearchPostsSkeleton.Params, models.AppBskyUnspeccedSearchPostsSkeleton.ParamsDict
        ],
        **kwargs: t.Any,
    ) -> 'models.AppBskyUnspeccedSearchPostsSkeleton.Response':
        """Backend Posts search, returning only skeleton.

        Args:
            params: Parameters.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.AppBskyUnspeccedSearchPostsSkeleton.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        params_model = get_or_create(params, models.AppBskyUnspeccedSearchPostsSkeleton.Params)
        response = self._client.invoke_query(
            'app.bsky.unspecced.searchPostsSkeleton', params=params_model, output_encoding='application/json', **kwargs
        )
        return get_response_model(response, models.AppBskyUnspeccedSearchPostsSkeleton.Response)


class ComNamespace(NamespaceBase):
    def __init__(self, client: 'ClientRaw') -> None:
        super().__init__(client)
        self.atproto = AtprotoNamespace(self._client)


class AtprotoNamespace(NamespaceBase):
    def __init__(self, client: 'ClientRaw') -> None:
        super().__init__(client)
        self.admin = AdminNamespace(self._client)
        self.identity = IdentityNamespace(self._client)
        self.label = LabelNamespace(self._client)
        self.moderation = ModerationNamespace(self._client)
        self.repo = RepoNamespace(self._client)
        self.server = ServerNamespace(self._client)
        self.sync = SyncNamespace(self._client)


class AdminNamespace(NamespaceBase):
    def disable_account_invites(
        self,
        data: t.Union[
            models.ComAtprotoAdminDisableAccountInvites.Data, models.ComAtprotoAdminDisableAccountInvites.DataDict
        ],
        **kwargs: t.Any,
    ) -> bool:
        """Disable an account from receiving new invite codes, but does not invalidate existing codes.

        Args:
            data: Input data.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`bool`: Success status.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        data_model = get_or_create(data, models.ComAtprotoAdminDisableAccountInvites.Data)
        response = self._client.invoke_procedure(
            'com.atproto.admin.disableAccountInvites', data=data_model, input_encoding='application/json', **kwargs
        )
        return get_response_model(response, bool)

    def disable_invite_codes(
        self,
        data: t.Optional[
            t.Union[models.ComAtprotoAdminDisableInviteCodes.Data, models.ComAtprotoAdminDisableInviteCodes.DataDict]
        ] = None,
        **kwargs: t.Any,
    ) -> bool:
        """Disable some set of codes and/or all codes associated with a set of users.

        Args:
            data: Input data.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`bool`: Success status.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        data_model = get_or_create(data, models.ComAtprotoAdminDisableInviteCodes.Data)
        response = self._client.invoke_procedure(
            'com.atproto.admin.disableInviteCodes', data=data_model, input_encoding='application/json', **kwargs
        )
        return get_response_model(response, bool)

    def enable_account_invites(
        self,
        data: t.Union[
            models.ComAtprotoAdminEnableAccountInvites.Data, models.ComAtprotoAdminEnableAccountInvites.DataDict
        ],
        **kwargs: t.Any,
    ) -> bool:
        """Re-enable an accounts ability to receive invite codes.

        Args:
            data: Input data.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`bool`: Success status.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        data_model = get_or_create(data, models.ComAtprotoAdminEnableAccountInvites.Data)
        response = self._client.invoke_procedure(
            'com.atproto.admin.enableAccountInvites', data=data_model, input_encoding='application/json', **kwargs
        )
        return get_response_model(response, bool)

    def get_account_info(
        self,
        params: t.Union[models.ComAtprotoAdminGetAccountInfo.Params, models.ComAtprotoAdminGetAccountInfo.ParamsDict],
        **kwargs: t.Any,
    ) -> 'models.ComAtprotoAdminDefs.AccountView':
        """View details about an account.

        Args:
            params: Parameters.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.ComAtprotoAdminDefs.AccountView`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        params_model = get_or_create(params, models.ComAtprotoAdminGetAccountInfo.Params)
        response = self._client.invoke_query(
            'com.atproto.admin.getAccountInfo', params=params_model, output_encoding='application/json', **kwargs
        )
        return get_response_model(response, models.ComAtprotoAdminDefs.AccountView)

    def get_invite_codes(
        self,
        params: t.Optional[
            t.Union[models.ComAtprotoAdminGetInviteCodes.Params, models.ComAtprotoAdminGetInviteCodes.ParamsDict]
        ] = None,
        **kwargs: t.Any,
    ) -> 'models.ComAtprotoAdminGetInviteCodes.Response':
        """Admin view of invite codes.

        Args:
            params: Parameters.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.ComAtprotoAdminGetInviteCodes.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        params_model = get_or_create(params, models.ComAtprotoAdminGetInviteCodes.Params)
        response = self._client.invoke_query(
            'com.atproto.admin.getInviteCodes', params=params_model, output_encoding='application/json', **kwargs
        )
        return get_response_model(response, models.ComAtprotoAdminGetInviteCodes.Response)

    def get_moderation_action(
        self,
        params: t.Union[
            models.ComAtprotoAdminGetModerationAction.Params, models.ComAtprotoAdminGetModerationAction.ParamsDict
        ],
        **kwargs: t.Any,
    ) -> 'models.ComAtprotoAdminDefs.ActionViewDetail':
        """View details about a moderation action.

        Args:
            params: Parameters.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.ComAtprotoAdminDefs.ActionViewDetail`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        params_model = get_or_create(params, models.ComAtprotoAdminGetModerationAction.Params)
        response = self._client.invoke_query(
            'com.atproto.admin.getModerationAction', params=params_model, output_encoding='application/json', **kwargs
        )
        return get_response_model(response, models.ComAtprotoAdminDefs.ActionViewDetail)

    def get_moderation_actions(
        self,
        params: t.Optional[
            t.Union[
                models.ComAtprotoAdminGetModerationActions.Params, models.ComAtprotoAdminGetModerationActions.ParamsDict
            ]
        ] = None,
        **kwargs: t.Any,
    ) -> 'models.ComAtprotoAdminGetModerationActions.Response':
        """List moderation actions related to a subject.

        Args:
            params: Parameters.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.ComAtprotoAdminGetModerationActions.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        params_model = get_or_create(params, models.ComAtprotoAdminGetModerationActions.Params)
        response = self._client.invoke_query(
            'com.atproto.admin.getModerationActions', params=params_model, output_encoding='application/json', **kwargs
        )
        return get_response_model(response, models.ComAtprotoAdminGetModerationActions.Response)

    def get_moderation_report(
        self,
        params: t.Union[
            models.ComAtprotoAdminGetModerationReport.Params, models.ComAtprotoAdminGetModerationReport.ParamsDict
        ],
        **kwargs: t.Any,
    ) -> 'models.ComAtprotoAdminDefs.ReportViewDetail':
        """View details about a moderation report.

        Args:
            params: Parameters.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.ComAtprotoAdminDefs.ReportViewDetail`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        params_model = get_or_create(params, models.ComAtprotoAdminGetModerationReport.Params)
        response = self._client.invoke_query(
            'com.atproto.admin.getModerationReport', params=params_model, output_encoding='application/json', **kwargs
        )
        return get_response_model(response, models.ComAtprotoAdminDefs.ReportViewDetail)

    def get_moderation_reports(
        self,
        params: t.Optional[
            t.Union[
                models.ComAtprotoAdminGetModerationReports.Params, models.ComAtprotoAdminGetModerationReports.ParamsDict
            ]
        ] = None,
        **kwargs: t.Any,
    ) -> 'models.ComAtprotoAdminGetModerationReports.Response':
        """List moderation reports related to a subject.

        Args:
            params: Parameters.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.ComAtprotoAdminGetModerationReports.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        params_model = get_or_create(params, models.ComAtprotoAdminGetModerationReports.Params)
        response = self._client.invoke_query(
            'com.atproto.admin.getModerationReports', params=params_model, output_encoding='application/json', **kwargs
        )
        return get_response_model(response, models.ComAtprotoAdminGetModerationReports.Response)

    def get_record(
        self,
        params: t.Union[models.ComAtprotoAdminGetRecord.Params, models.ComAtprotoAdminGetRecord.ParamsDict],
        **kwargs: t.Any,
    ) -> 'models.ComAtprotoAdminDefs.RecordViewDetail':
        """View details about a record.

        Args:
            params: Parameters.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.ComAtprotoAdminDefs.RecordViewDetail`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        params_model = get_or_create(params, models.ComAtprotoAdminGetRecord.Params)
        response = self._client.invoke_query(
            'com.atproto.admin.getRecord', params=params_model, output_encoding='application/json', **kwargs
        )
        return get_response_model(response, models.ComAtprotoAdminDefs.RecordViewDetail)

    def get_repo(
        self,
        params: t.Union[models.ComAtprotoAdminGetRepo.Params, models.ComAtprotoAdminGetRepo.ParamsDict],
        **kwargs: t.Any,
    ) -> 'models.ComAtprotoAdminDefs.RepoViewDetail':
        """View details about a repository.

        Args:
            params: Parameters.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.ComAtprotoAdminDefs.RepoViewDetail`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        params_model = get_or_create(params, models.ComAtprotoAdminGetRepo.Params)
        response = self._client.invoke_query(
            'com.atproto.admin.getRepo', params=params_model, output_encoding='application/json', **kwargs
        )
        return get_response_model(response, models.ComAtprotoAdminDefs.RepoViewDetail)

    def get_subject_status(
        self,
        params: t.Optional[
            t.Union[models.ComAtprotoAdminGetSubjectStatus.Params, models.ComAtprotoAdminGetSubjectStatus.ParamsDict]
        ] = None,
        **kwargs: t.Any,
    ) -> 'models.ComAtprotoAdminGetSubjectStatus.Response':
        """Fetch the service-specific the admin status of a subject (account, record, or blob).

        Args:
            params: Parameters.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.ComAtprotoAdminGetSubjectStatus.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        params_model = get_or_create(params, models.ComAtprotoAdminGetSubjectStatus.Params)
        response = self._client.invoke_query(
            'com.atproto.admin.getSubjectStatus', params=params_model, output_encoding='application/json', **kwargs
        )
        return get_response_model(response, models.ComAtprotoAdminGetSubjectStatus.Response)

    def resolve_moderation_reports(
        self,
        data: t.Union[
            models.ComAtprotoAdminResolveModerationReports.Data, models.ComAtprotoAdminResolveModerationReports.DataDict
        ],
        **kwargs: t.Any,
    ) -> 'models.ComAtprotoAdminDefs.ActionView':
        """Resolve moderation reports by an action.

        Args:
            data: Input data.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.ComAtprotoAdminDefs.ActionView`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        data_model = get_or_create(data, models.ComAtprotoAdminResolveModerationReports.Data)
        response = self._client.invoke_procedure(
            'com.atproto.admin.resolveModerationReports',
            data=data_model,
            input_encoding='application/json',
            output_encoding='application/json',
            **kwargs,
        )
        return get_response_model(response, models.ComAtprotoAdminDefs.ActionView)

    def reverse_moderation_action(
        self,
        data: t.Union[
            models.ComAtprotoAdminReverseModerationAction.Data, models.ComAtprotoAdminReverseModerationAction.DataDict
        ],
        **kwargs: t.Any,
    ) -> 'models.ComAtprotoAdminDefs.ActionView':
        """Reverse a moderation action.

        Args:
            data: Input data.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.ComAtprotoAdminDefs.ActionView`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        data_model = get_or_create(data, models.ComAtprotoAdminReverseModerationAction.Data)
        response = self._client.invoke_procedure(
            'com.atproto.admin.reverseModerationAction',
            data=data_model,
            input_encoding='application/json',
            output_encoding='application/json',
            **kwargs,
        )
        return get_response_model(response, models.ComAtprotoAdminDefs.ActionView)

    def search_repos(
        self,
        params: t.Optional[
            t.Union[models.ComAtprotoAdminSearchRepos.Params, models.ComAtprotoAdminSearchRepos.ParamsDict]
        ] = None,
        **kwargs: t.Any,
    ) -> 'models.ComAtprotoAdminSearchRepos.Response':
        """Find repositories based on a search term.

        Args:
            params: Parameters.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.ComAtprotoAdminSearchRepos.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        params_model = get_or_create(params, models.ComAtprotoAdminSearchRepos.Params)
        response = self._client.invoke_query(
            'com.atproto.admin.searchRepos', params=params_model, output_encoding='application/json', **kwargs
        )
        return get_response_model(response, models.ComAtprotoAdminSearchRepos.Response)

    def send_email(
        self,
        data: t.Union[models.ComAtprotoAdminSendEmail.Data, models.ComAtprotoAdminSendEmail.DataDict],
        **kwargs: t.Any,
    ) -> 'models.ComAtprotoAdminSendEmail.Response':
        """Send email to a user's primary email address.

        Args:
            data: Input data.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.ComAtprotoAdminSendEmail.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        data_model = get_or_create(data, models.ComAtprotoAdminSendEmail.Data)
        response = self._client.invoke_procedure(
            'com.atproto.admin.sendEmail',
            data=data_model,
            input_encoding='application/json',
            output_encoding='application/json',
            **kwargs,
        )
        return get_response_model(response, models.ComAtprotoAdminSendEmail.Response)

    def take_moderation_action(
        self,
        data: t.Union[
            models.ComAtprotoAdminTakeModerationAction.Data, models.ComAtprotoAdminTakeModerationAction.DataDict
        ],
        **kwargs: t.Any,
    ) -> 'models.ComAtprotoAdminDefs.ActionView':
        """Take a moderation action on a repo.

        Args:
            data: Input data.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.ComAtprotoAdminDefs.ActionView`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        data_model = get_or_create(data, models.ComAtprotoAdminTakeModerationAction.Data)
        response = self._client.invoke_procedure(
            'com.atproto.admin.takeModerationAction',
            data=data_model,
            input_encoding='application/json',
            output_encoding='application/json',
            **kwargs,
        )
        return get_response_model(response, models.ComAtprotoAdminDefs.ActionView)

    def update_account_email(
        self,
        data: t.Union[models.ComAtprotoAdminUpdateAccountEmail.Data, models.ComAtprotoAdminUpdateAccountEmail.DataDict],
        **kwargs: t.Any,
    ) -> bool:
        """Administrative action to update an account's email.

        Args:
            data: Input data.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`bool`: Success status.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        data_model = get_or_create(data, models.ComAtprotoAdminUpdateAccountEmail.Data)
        response = self._client.invoke_procedure(
            'com.atproto.admin.updateAccountEmail', data=data_model, input_encoding='application/json', **kwargs
        )
        return get_response_model(response, bool)

    def update_account_handle(
        self,
        data: t.Union[
            models.ComAtprotoAdminUpdateAccountHandle.Data, models.ComAtprotoAdminUpdateAccountHandle.DataDict
        ],
        **kwargs: t.Any,
    ) -> bool:
        """Administrative action to update an account's handle.

        Args:
            data: Input data.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`bool`: Success status.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        data_model = get_or_create(data, models.ComAtprotoAdminUpdateAccountHandle.Data)
        response = self._client.invoke_procedure(
            'com.atproto.admin.updateAccountHandle', data=data_model, input_encoding='application/json', **kwargs
        )
        return get_response_model(response, bool)

    def update_subject_status(
        self,
        data: t.Union[
            models.ComAtprotoAdminUpdateSubjectStatus.Data, models.ComAtprotoAdminUpdateSubjectStatus.DataDict
        ],
        **kwargs: t.Any,
    ) -> 'models.ComAtprotoAdminUpdateSubjectStatus.Response':
        """Update the service-specific admin status of a subject (account, record, or blob).

        Args:
            data: Input data.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.ComAtprotoAdminUpdateSubjectStatus.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        data_model = get_or_create(data, models.ComAtprotoAdminUpdateSubjectStatus.Data)
        response = self._client.invoke_procedure(
            'com.atproto.admin.updateSubjectStatus',
            data=data_model,
            input_encoding='application/json',
            output_encoding='application/json',
            **kwargs,
        )
        return get_response_model(response, models.ComAtprotoAdminUpdateSubjectStatus.Response)


class IdentityNamespace(NamespaceBase):
    def resolve_handle(
        self,
        params: t.Union[
            models.ComAtprotoIdentityResolveHandle.Params, models.ComAtprotoIdentityResolveHandle.ParamsDict
        ],
        **kwargs: t.Any,
    ) -> 'models.ComAtprotoIdentityResolveHandle.Response':
        """Provides the DID of a repo.

        Args:
            params: Parameters.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.ComAtprotoIdentityResolveHandle.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        params_model = get_or_create(params, models.ComAtprotoIdentityResolveHandle.Params)
        response = self._client.invoke_query(
            'com.atproto.identity.resolveHandle', params=params_model, output_encoding='application/json', **kwargs
        )
        return get_response_model(response, models.ComAtprotoIdentityResolveHandle.Response)

    def update_handle(
        self,
        data: t.Union[models.ComAtprotoIdentityUpdateHandle.Data, models.ComAtprotoIdentityUpdateHandle.DataDict],
        **kwargs: t.Any,
    ) -> bool:
        """Updates the handle of the account.

        Args:
            data: Input data.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`bool`: Success status.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        data_model = get_or_create(data, models.ComAtprotoIdentityUpdateHandle.Data)
        response = self._client.invoke_procedure(
            'com.atproto.identity.updateHandle', data=data_model, input_encoding='application/json', **kwargs
        )
        return get_response_model(response, bool)


class LabelNamespace(NamespaceBase):
    def query_labels(
        self,
        params: t.Union[models.ComAtprotoLabelQueryLabels.Params, models.ComAtprotoLabelQueryLabels.ParamsDict],
        **kwargs: t.Any,
    ) -> 'models.ComAtprotoLabelQueryLabels.Response':
        """Find labels relevant to the provided URI patterns.

        Args:
            params: Parameters.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.ComAtprotoLabelQueryLabels.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        params_model = get_or_create(params, models.ComAtprotoLabelQueryLabels.Params)
        response = self._client.invoke_query(
            'com.atproto.label.queryLabels', params=params_model, output_encoding='application/json', **kwargs
        )
        return get_response_model(response, models.ComAtprotoLabelQueryLabels.Response)


class ModerationNamespace(NamespaceBase):
    def create_report(
        self,
        data: t.Union[models.ComAtprotoModerationCreateReport.Data, models.ComAtprotoModerationCreateReport.DataDict],
        **kwargs: t.Any,
    ) -> 'models.ComAtprotoModerationCreateReport.Response':
        """Report a repo or a record.

        Args:
            data: Input data.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.ComAtprotoModerationCreateReport.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        data_model = get_or_create(data, models.ComAtprotoModerationCreateReport.Data)
        response = self._client.invoke_procedure(
            'com.atproto.moderation.createReport',
            data=data_model,
            input_encoding='application/json',
            output_encoding='application/json',
            **kwargs,
        )
        return get_response_model(response, models.ComAtprotoModerationCreateReport.Response)


class RepoNamespace(NamespaceBase):
    def apply_writes(
        self,
        data: t.Union[models.ComAtprotoRepoApplyWrites.Data, models.ComAtprotoRepoApplyWrites.DataDict],
        **kwargs: t.Any,
    ) -> bool:
        """Apply a batch transaction of creates, updates, and deletes.

        Args:
            data: Input data.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`bool`: Success status.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        data_model = get_or_create(data, models.ComAtprotoRepoApplyWrites.Data)
        response = self._client.invoke_procedure(
            'com.atproto.repo.applyWrites', data=data_model, input_encoding='application/json', **kwargs
        )
        return get_response_model(response, bool)

    def create_record(
        self,
        data: t.Union[models.ComAtprotoRepoCreateRecord.Data, models.ComAtprotoRepoCreateRecord.DataDict],
        **kwargs: t.Any,
    ) -> 'models.ComAtprotoRepoCreateRecord.Response':
        """Create a new record.

        Args:
            data: Input data.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.ComAtprotoRepoCreateRecord.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        data_model = get_or_create(data, models.ComAtprotoRepoCreateRecord.Data)
        response = self._client.invoke_procedure(
            'com.atproto.repo.createRecord',
            data=data_model,
            input_encoding='application/json',
            output_encoding='application/json',
            **kwargs,
        )
        return get_response_model(response, models.ComAtprotoRepoCreateRecord.Response)

    def delete_record(
        self,
        data: t.Union[models.ComAtprotoRepoDeleteRecord.Data, models.ComAtprotoRepoDeleteRecord.DataDict],
        **kwargs: t.Any,
    ) -> bool:
        """Delete a record, or ensure it doesn't exist.

        Args:
            data: Input data.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`bool`: Success status.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        data_model = get_or_create(data, models.ComAtprotoRepoDeleteRecord.Data)
        response = self._client.invoke_procedure(
            'com.atproto.repo.deleteRecord', data=data_model, input_encoding='application/json', **kwargs
        )
        return get_response_model(response, bool)

    def describe_repo(
        self,
        params: t.Union[models.ComAtprotoRepoDescribeRepo.Params, models.ComAtprotoRepoDescribeRepo.ParamsDict],
        **kwargs: t.Any,
    ) -> 'models.ComAtprotoRepoDescribeRepo.Response':
        """Get information about the repo, including the list of collections.

        Args:
            params: Parameters.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.ComAtprotoRepoDescribeRepo.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        params_model = get_or_create(params, models.ComAtprotoRepoDescribeRepo.Params)
        response = self._client.invoke_query(
            'com.atproto.repo.describeRepo', params=params_model, output_encoding='application/json', **kwargs
        )
        return get_response_model(response, models.ComAtprotoRepoDescribeRepo.Response)

    def get_record(
        self,
        params: t.Union[models.ComAtprotoRepoGetRecord.Params, models.ComAtprotoRepoGetRecord.ParamsDict],
        **kwargs: t.Any,
    ) -> 'models.ComAtprotoRepoGetRecord.Response':
        """Get a record.

        Args:
            params: Parameters.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.ComAtprotoRepoGetRecord.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        params_model = get_or_create(params, models.ComAtprotoRepoGetRecord.Params)
        response = self._client.invoke_query(
            'com.atproto.repo.getRecord', params=params_model, output_encoding='application/json', **kwargs
        )
        return get_response_model(response, models.ComAtprotoRepoGetRecord.Response)

    def list_records(
        self,
        params: t.Union[models.ComAtprotoRepoListRecords.Params, models.ComAtprotoRepoListRecords.ParamsDict],
        **kwargs: t.Any,
    ) -> 'models.ComAtprotoRepoListRecords.Response':
        """List a range of records in a collection.

        Args:
            params: Parameters.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.ComAtprotoRepoListRecords.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        params_model = get_or_create(params, models.ComAtprotoRepoListRecords.Params)
        response = self._client.invoke_query(
            'com.atproto.repo.listRecords', params=params_model, output_encoding='application/json', **kwargs
        )
        return get_response_model(response, models.ComAtprotoRepoListRecords.Response)

    def put_record(
        self,
        data: t.Union[models.ComAtprotoRepoPutRecord.Data, models.ComAtprotoRepoPutRecord.DataDict],
        **kwargs: t.Any,
    ) -> 'models.ComAtprotoRepoPutRecord.Response':
        """Write a record, creating or updating it as needed.

        Args:
            data: Input data.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.ComAtprotoRepoPutRecord.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        data_model = get_or_create(data, models.ComAtprotoRepoPutRecord.Data)
        response = self._client.invoke_procedure(
            'com.atproto.repo.putRecord',
            data=data_model,
            input_encoding='application/json',
            output_encoding='application/json',
            **kwargs,
        )
        return get_response_model(response, models.ComAtprotoRepoPutRecord.Response)

    def upload_blob(
        self, data: 'models.ComAtprotoRepoUploadBlob.Data', **kwargs: t.Any
    ) -> 'models.ComAtprotoRepoUploadBlob.Response':
        """Upload a new blob to be added to repo in a later request.

        Args:
            data: Input data alias.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.ComAtprotoRepoUploadBlob.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        response = self._client.invoke_procedure(
            'com.atproto.repo.uploadBlob', data=data, input_encoding='*/*', output_encoding='application/json', **kwargs
        )
        return get_response_model(response, models.ComAtprotoRepoUploadBlob.Response)


class ServerNamespace(NamespaceBase):
    def confirm_email(
        self,
        data: t.Union[models.ComAtprotoServerConfirmEmail.Data, models.ComAtprotoServerConfirmEmail.DataDict],
        **kwargs: t.Any,
    ) -> bool:
        """Confirm an email using a token from com.atproto.server.requestEmailConfirmation.

        Args:
            data: Input data.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`bool`: Success status.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        data_model = get_or_create(data, models.ComAtprotoServerConfirmEmail.Data)
        response = self._client.invoke_procedure(
            'com.atproto.server.confirmEmail', data=data_model, input_encoding='application/json', **kwargs
        )
        return get_response_model(response, bool)

    def create_account(
        self,
        data: t.Union[models.ComAtprotoServerCreateAccount.Data, models.ComAtprotoServerCreateAccount.DataDict],
        **kwargs: t.Any,
    ) -> 'models.ComAtprotoServerCreateAccount.Response':
        """Create an account.

        Args:
            data: Input data.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.ComAtprotoServerCreateAccount.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        data_model = get_or_create(data, models.ComAtprotoServerCreateAccount.Data)
        response = self._client.invoke_procedure(
            'com.atproto.server.createAccount',
            data=data_model,
            input_encoding='application/json',
            output_encoding='application/json',
            **kwargs,
        )
        return get_response_model(response, models.ComAtprotoServerCreateAccount.Response)

    def create_app_password(
        self,
        data: t.Union[models.ComAtprotoServerCreateAppPassword.Data, models.ComAtprotoServerCreateAppPassword.DataDict],
        **kwargs: t.Any,
    ) -> 'models.ComAtprotoServerCreateAppPassword.AppPassword':
        """Create an app-specific password.

        Args:
            data: Input data.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.ComAtprotoServerCreateAppPassword.AppPassword`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        data_model = get_or_create(data, models.ComAtprotoServerCreateAppPassword.Data)
        response = self._client.invoke_procedure(
            'com.atproto.server.createAppPassword',
            data=data_model,
            input_encoding='application/json',
            output_encoding='application/json',
            **kwargs,
        )
        return get_response_model(response, models.ComAtprotoServerCreateAppPassword.AppPassword)

    def create_invite_code(
        self,
        data: t.Union[models.ComAtprotoServerCreateInviteCode.Data, models.ComAtprotoServerCreateInviteCode.DataDict],
        **kwargs: t.Any,
    ) -> 'models.ComAtprotoServerCreateInviteCode.Response':
        """Create an invite code.

        Args:
            data: Input data.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.ComAtprotoServerCreateInviteCode.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        data_model = get_or_create(data, models.ComAtprotoServerCreateInviteCode.Data)
        response = self._client.invoke_procedure(
            'com.atproto.server.createInviteCode',
            data=data_model,
            input_encoding='application/json',
            output_encoding='application/json',
            **kwargs,
        )
        return get_response_model(response, models.ComAtprotoServerCreateInviteCode.Response)

    def create_invite_codes(
        self,
        data: t.Union[models.ComAtprotoServerCreateInviteCodes.Data, models.ComAtprotoServerCreateInviteCodes.DataDict],
        **kwargs: t.Any,
    ) -> 'models.ComAtprotoServerCreateInviteCodes.Response':
        """Create an invite code.

        Args:
            data: Input data.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.ComAtprotoServerCreateInviteCodes.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        data_model = get_or_create(data, models.ComAtprotoServerCreateInviteCodes.Data)
        response = self._client.invoke_procedure(
            'com.atproto.server.createInviteCodes',
            data=data_model,
            input_encoding='application/json',
            output_encoding='application/json',
            **kwargs,
        )
        return get_response_model(response, models.ComAtprotoServerCreateInviteCodes.Response)

    def create_session(
        self,
        data: t.Union[models.ComAtprotoServerCreateSession.Data, models.ComAtprotoServerCreateSession.DataDict],
        **kwargs: t.Any,
    ) -> 'models.ComAtprotoServerCreateSession.Response':
        """Create an authentication session.

        Args:
            data: Input data.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.ComAtprotoServerCreateSession.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        data_model = get_or_create(data, models.ComAtprotoServerCreateSession.Data)
        response = self._client.invoke_procedure(
            'com.atproto.server.createSession',
            data=data_model,
            input_encoding='application/json',
            output_encoding='application/json',
            **kwargs,
        )
        return get_response_model(response, models.ComAtprotoServerCreateSession.Response)

    def delete_account(
        self,
        data: t.Union[models.ComAtprotoServerDeleteAccount.Data, models.ComAtprotoServerDeleteAccount.DataDict],
        **kwargs: t.Any,
    ) -> bool:
        """Delete a user account with a token and password.

        Args:
            data: Input data.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`bool`: Success status.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        data_model = get_or_create(data, models.ComAtprotoServerDeleteAccount.Data)
        response = self._client.invoke_procedure(
            'com.atproto.server.deleteAccount', data=data_model, input_encoding='application/json', **kwargs
        )
        return get_response_model(response, bool)

    def delete_session(self, **kwargs: t.Any) -> bool:
        """Delete the current session.

        Args:
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`bool`: Success status.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        response = self._client.invoke_procedure('com.atproto.server.deleteSession', **kwargs)
        return get_response_model(response, bool)

    def describe_server(self, **kwargs: t.Any) -> 'models.ComAtprotoServerDescribeServer.Response':
        """Get a document describing the service's accounts configuration.

        Args:
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.ComAtprotoServerDescribeServer.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        response = self._client.invoke_query(
            'com.atproto.server.describeServer', output_encoding='application/json', **kwargs
        )
        return get_response_model(response, models.ComAtprotoServerDescribeServer.Response)

    def get_account_invite_codes(
        self,
        params: t.Optional[
            t.Union[
                models.ComAtprotoServerGetAccountInviteCodes.Params,
                models.ComAtprotoServerGetAccountInviteCodes.ParamsDict,
            ]
        ] = None,
        **kwargs: t.Any,
    ) -> 'models.ComAtprotoServerGetAccountInviteCodes.Response':
        """Get all invite codes for a given account.

        Args:
            params: Parameters.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.ComAtprotoServerGetAccountInviteCodes.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        params_model = get_or_create(params, models.ComAtprotoServerGetAccountInviteCodes.Params)
        response = self._client.invoke_query(
            'com.atproto.server.getAccountInviteCodes',
            params=params_model,
            output_encoding='application/json',
            **kwargs,
        )
        return get_response_model(response, models.ComAtprotoServerGetAccountInviteCodes.Response)

    def get_session(self, **kwargs: t.Any) -> 'models.ComAtprotoServerGetSession.Response':
        """Get information about the current session.

        Args:
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.ComAtprotoServerGetSession.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        response = self._client.invoke_query(
            'com.atproto.server.getSession', output_encoding='application/json', **kwargs
        )
        return get_response_model(response, models.ComAtprotoServerGetSession.Response)

    def list_app_passwords(self, **kwargs: t.Any) -> 'models.ComAtprotoServerListAppPasswords.Response':
        """List all app-specific passwords.

        Args:
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.ComAtprotoServerListAppPasswords.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        response = self._client.invoke_query(
            'com.atproto.server.listAppPasswords', output_encoding='application/json', **kwargs
        )
        return get_response_model(response, models.ComAtprotoServerListAppPasswords.Response)

    def refresh_session(self, **kwargs: t.Any) -> 'models.ComAtprotoServerRefreshSession.Response':
        """Refresh an authentication session.

        Args:
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.ComAtprotoServerRefreshSession.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        response = self._client.invoke_procedure(
            'com.atproto.server.refreshSession', output_encoding='application/json', **kwargs
        )
        return get_response_model(response, models.ComAtprotoServerRefreshSession.Response)

    def request_account_delete(self, **kwargs: t.Any) -> bool:
        """Initiate a user account deletion via email.

        Args:
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`bool`: Success status.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        response = self._client.invoke_procedure('com.atproto.server.requestAccountDelete', **kwargs)
        return get_response_model(response, bool)

    def request_email_confirmation(self, **kwargs: t.Any) -> bool:
        """Request an email with a code to confirm ownership of email.

        Args:
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`bool`: Success status.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        response = self._client.invoke_procedure('com.atproto.server.requestEmailConfirmation', **kwargs)
        return get_response_model(response, bool)

    def request_email_update(self, **kwargs: t.Any) -> 'models.ComAtprotoServerRequestEmailUpdate.Response':
        """Request a token in order to update email.

        Args:
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.ComAtprotoServerRequestEmailUpdate.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        response = self._client.invoke_procedure(
            'com.atproto.server.requestEmailUpdate', output_encoding='application/json', **kwargs
        )
        return get_response_model(response, models.ComAtprotoServerRequestEmailUpdate.Response)

    def request_password_reset(
        self,
        data: t.Union[
            models.ComAtprotoServerRequestPasswordReset.Data, models.ComAtprotoServerRequestPasswordReset.DataDict
        ],
        **kwargs: t.Any,
    ) -> bool:
        """Initiate a user account password reset via email.

        Args:
            data: Input data.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`bool`: Success status.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        data_model = get_or_create(data, models.ComAtprotoServerRequestPasswordReset.Data)
        response = self._client.invoke_procedure(
            'com.atproto.server.requestPasswordReset', data=data_model, input_encoding='application/json', **kwargs
        )
        return get_response_model(response, bool)

    def reserve_signing_key(
        self,
        data: t.Optional[
            t.Union[models.ComAtprotoServerReserveSigningKey.Data, models.ComAtprotoServerReserveSigningKey.DataDict]
        ] = None,
        **kwargs: t.Any,
    ) -> 'models.ComAtprotoServerReserveSigningKey.Response':
        """Reserve a repo signing key for account creation.

        Args:
            data: Input data.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.ComAtprotoServerReserveSigningKey.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        data_model = get_or_create(data, models.ComAtprotoServerReserveSigningKey.Data)
        response = self._client.invoke_procedure(
            'com.atproto.server.reserveSigningKey',
            data=data_model,
            input_encoding='application/json',
            output_encoding='application/json',
            **kwargs,
        )
        return get_response_model(response, models.ComAtprotoServerReserveSigningKey.Response)

    def reset_password(
        self,
        data: t.Union[models.ComAtprotoServerResetPassword.Data, models.ComAtprotoServerResetPassword.DataDict],
        **kwargs: t.Any,
    ) -> bool:
        """Reset a user account password using a token.

        Args:
            data: Input data.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`bool`: Success status.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        data_model = get_or_create(data, models.ComAtprotoServerResetPassword.Data)
        response = self._client.invoke_procedure(
            'com.atproto.server.resetPassword', data=data_model, input_encoding='application/json', **kwargs
        )
        return get_response_model(response, bool)

    def revoke_app_password(
        self,
        data: t.Union[models.ComAtprotoServerRevokeAppPassword.Data, models.ComAtprotoServerRevokeAppPassword.DataDict],
        **kwargs: t.Any,
    ) -> bool:
        """Revoke an app-specific password by name.

        Args:
            data: Input data.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`bool`: Success status.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        data_model = get_or_create(data, models.ComAtprotoServerRevokeAppPassword.Data)
        response = self._client.invoke_procedure(
            'com.atproto.server.revokeAppPassword', data=data_model, input_encoding='application/json', **kwargs
        )
        return get_response_model(response, bool)

    def update_email(
        self,
        data: t.Union[models.ComAtprotoServerUpdateEmail.Data, models.ComAtprotoServerUpdateEmail.DataDict],
        **kwargs: t.Any,
    ) -> bool:
        """Update an account's email.

        Args:
            data: Input data.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`bool`: Success status.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        data_model = get_or_create(data, models.ComAtprotoServerUpdateEmail.Data)
        response = self._client.invoke_procedure(
            'com.atproto.server.updateEmail', data=data_model, input_encoding='application/json', **kwargs
        )
        return get_response_model(response, bool)


class SyncNamespace(NamespaceBase):
    def get_blob(
        self,
        params: t.Union[models.ComAtprotoSyncGetBlob.Params, models.ComAtprotoSyncGetBlob.ParamsDict],
        **kwargs: t.Any,
    ) -> 'models.ComAtprotoSyncGetBlob.Response':
        """Get a blob associated with a given repo.

        Args:
            params: Parameters.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.ComAtprotoSyncGetBlob.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        params_model = get_or_create(params, models.ComAtprotoSyncGetBlob.Params)
        response = self._client.invoke_query(
            'com.atproto.sync.getBlob', params=params_model, output_encoding='*/*', **kwargs
        )
        return get_response_model(response, models.ComAtprotoSyncGetBlob.Response)

    def get_blocks(
        self,
        params: t.Union[models.ComAtprotoSyncGetBlocks.Params, models.ComAtprotoSyncGetBlocks.ParamsDict],
        **kwargs: t.Any,
    ) -> 'models.ComAtprotoSyncGetBlocks.Response':
        """Gets blocks from a given repo.

        Args:
            params: Parameters.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.ComAtprotoSyncGetBlocks.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        params_model = get_or_create(params, models.ComAtprotoSyncGetBlocks.Params)
        response = self._client.invoke_query(
            'com.atproto.sync.getBlocks', params=params_model, output_encoding='application/vnd.ipld.car', **kwargs
        )
        return get_response_model(response, models.ComAtprotoSyncGetBlocks.Response)

    def get_checkout(
        self,
        params: t.Union[models.ComAtprotoSyncGetCheckout.Params, models.ComAtprotoSyncGetCheckout.ParamsDict],
        **kwargs: t.Any,
    ) -> 'models.ComAtprotoSyncGetCheckout.Response':
        """DEPRECATED - please use com.atproto.sync.getRepo instead.

        Args:
            params: Parameters.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.ComAtprotoSyncGetCheckout.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        params_model = get_or_create(params, models.ComAtprotoSyncGetCheckout.Params)
        response = self._client.invoke_query(
            'com.atproto.sync.getCheckout', params=params_model, output_encoding='application/vnd.ipld.car', **kwargs
        )
        return get_response_model(response, models.ComAtprotoSyncGetCheckout.Response)

    def get_head(
        self,
        params: t.Union[models.ComAtprotoSyncGetHead.Params, models.ComAtprotoSyncGetHead.ParamsDict],
        **kwargs: t.Any,
    ) -> 'models.ComAtprotoSyncGetHead.Response':
        """DEPRECATED - please use com.atproto.sync.getLatestCommit instead.

        Args:
            params: Parameters.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.ComAtprotoSyncGetHead.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        params_model = get_or_create(params, models.ComAtprotoSyncGetHead.Params)
        response = self._client.invoke_query(
            'com.atproto.sync.getHead', params=params_model, output_encoding='application/json', **kwargs
        )
        return get_response_model(response, models.ComAtprotoSyncGetHead.Response)

    def get_latest_commit(
        self,
        params: t.Union[models.ComAtprotoSyncGetLatestCommit.Params, models.ComAtprotoSyncGetLatestCommit.ParamsDict],
        **kwargs: t.Any,
    ) -> 'models.ComAtprotoSyncGetLatestCommit.Response':
        """Gets the current commit CID & revision of the repo.

        Args:
            params: Parameters.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.ComAtprotoSyncGetLatestCommit.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        params_model = get_or_create(params, models.ComAtprotoSyncGetLatestCommit.Params)
        response = self._client.invoke_query(
            'com.atproto.sync.getLatestCommit', params=params_model, output_encoding='application/json', **kwargs
        )
        return get_response_model(response, models.ComAtprotoSyncGetLatestCommit.Response)

    def get_record(
        self,
        params: t.Union[models.ComAtprotoSyncGetRecord.Params, models.ComAtprotoSyncGetRecord.ParamsDict],
        **kwargs: t.Any,
    ) -> 'models.ComAtprotoSyncGetRecord.Response':
        """Gets blocks needed for existence or non-existence of record.

        Args:
            params: Parameters.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.ComAtprotoSyncGetRecord.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        params_model = get_or_create(params, models.ComAtprotoSyncGetRecord.Params)
        response = self._client.invoke_query(
            'com.atproto.sync.getRecord', params=params_model, output_encoding='application/vnd.ipld.car', **kwargs
        )
        return get_response_model(response, models.ComAtprotoSyncGetRecord.Response)

    def get_repo(
        self,
        params: t.Union[models.ComAtprotoSyncGetRepo.Params, models.ComAtprotoSyncGetRepo.ParamsDict],
        **kwargs: t.Any,
    ) -> 'models.ComAtprotoSyncGetRepo.Response':
        """Gets the did's repo, optionally catching up from a specific revision.

        Args:
            params: Parameters.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.ComAtprotoSyncGetRepo.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        params_model = get_or_create(params, models.ComAtprotoSyncGetRepo.Params)
        response = self._client.invoke_query(
            'com.atproto.sync.getRepo', params=params_model, output_encoding='application/vnd.ipld.car', **kwargs
        )
        return get_response_model(response, models.ComAtprotoSyncGetRepo.Response)

    def list_blobs(
        self,
        params: t.Union[models.ComAtprotoSyncListBlobs.Params, models.ComAtprotoSyncListBlobs.ParamsDict],
        **kwargs: t.Any,
    ) -> 'models.ComAtprotoSyncListBlobs.Response':
        """List blob cids since some revision.

        Args:
            params: Parameters.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.ComAtprotoSyncListBlobs.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        params_model = get_or_create(params, models.ComAtprotoSyncListBlobs.Params)
        response = self._client.invoke_query(
            'com.atproto.sync.listBlobs', params=params_model, output_encoding='application/json', **kwargs
        )
        return get_response_model(response, models.ComAtprotoSyncListBlobs.Response)

    def list_repos(
        self,
        params: t.Optional[
            t.Union[models.ComAtprotoSyncListRepos.Params, models.ComAtprotoSyncListRepos.ParamsDict]
        ] = None,
        **kwargs: t.Any,
    ) -> 'models.ComAtprotoSyncListRepos.Response':
        """List dids and root cids of hosted repos.

        Args:
            params: Parameters.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`models.ComAtprotoSyncListRepos.Response`: Output model.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        params_model = get_or_create(params, models.ComAtprotoSyncListRepos.Params)
        response = self._client.invoke_query(
            'com.atproto.sync.listRepos', params=params_model, output_encoding='application/json', **kwargs
        )
        return get_response_model(response, models.ComAtprotoSyncListRepos.Response)

    def notify_of_update(
        self,
        data: t.Union[models.ComAtprotoSyncNotifyOfUpdate.Data, models.ComAtprotoSyncNotifyOfUpdate.DataDict],
        **kwargs: t.Any,
    ) -> bool:
        """Notify a crawling service of a recent update. Often when a long break between updates causes the connection with the crawling service to break.

        Args:
            data: Input data.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`bool`: Success status.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        data_model = get_or_create(data, models.ComAtprotoSyncNotifyOfUpdate.Data)
        response = self._client.invoke_procedure(
            'com.atproto.sync.notifyOfUpdate', data=data_model, input_encoding='application/json', **kwargs
        )
        return get_response_model(response, bool)

    def request_crawl(
        self,
        data: t.Union[models.ComAtprotoSyncRequestCrawl.Data, models.ComAtprotoSyncRequestCrawl.DataDict],
        **kwargs: t.Any,
    ) -> bool:
        """Request a service to persistently crawl hosted repos.

        Args:
            data: Input data.
            **kwargs: Arbitrary arguments to HTTP request.

        Returns:
            :obj:`bool`: Success status.

        Raises:
            :class:`atproto.exceptions.AtProtocolError`: Base exception.
        """

        data_model = get_or_create(data, models.ComAtprotoSyncRequestCrawl.Data)
        response = self._client.invoke_procedure(
            'com.atproto.sync.requestCrawl', data=data_model, input_encoding='application/json', **kwargs
        )
        return get_response_model(response, bool)
