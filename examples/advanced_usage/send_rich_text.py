from atproto import Client, models

# to send links as "link card" or "quote post" look at the send_embed.py example


def main():
    client = Client()
    client.login('my-handle', 'my-password')

    text = 'example link'
    url = 'https://google.com'

    facets = [
        models.AppBskyRichtextFacet.Main(
            features=[models.AppBskyRichtextFacet.Link(uri=url)],
            # we should pass when our link starts and ends in the text
            # the example below selects all the text
            index=models.AppBskyRichtextFacet.ByteSlice(byte_start=0, byte_end=len(text.encode('UTF-8'))),
        )
    ]

    client.com.atproto.repo.create_record(
        models.ComAtprotoRepoCreateRecord.Data(
            repo=client.me.did,  # or any another DID
            collection=models.ids.AppBskyFeedPost,
            record=models.AppBskyFeedPost.Main(created_at=client.get_current_time_iso(), text=text, facets=facets),
        )
    )


if __name__ == '__main__':
    main()
