curl --location --request POST 'http://54.201.32.68/v1/datasets/0fb708b3-ccb4-4b32-9508-520fe2b20785/document/create-by-file' \
  --header 'Authorization: Bearer dataset-dkdM6HEzAVbI62LdDOaJZ2LY' \
  --form 'data={"indexing_technique":"high_quality","process_rule":{"rules":{"pre_processing_rules":[{"id":"remove_extra_spaces","enabled":true},{"id":"remove_urls_emails","enabled":true}],"segmentation":{"separator":"###","max_tokens":500}},"mode":"custom"}};type=application/json' \
  --form 'file=@./人工智慧學程活動規劃.pdf;type=application/pdf'
