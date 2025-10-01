def main():
    c = input("File name: ").strip()

    if"."in c:
        x, y = c.split(".",1)
        match y :
            case"aac":
                print("audio/aac")

            case"abw":
                print("application/x-abiword")
    
            case"apng":
                print("image/apng")
    
            case"arc":
                print("application/x-freearc")
    
            case"avif":
                print("image/avif")
            case"avi":
                print("video/x-msvideo")
            case"azw":
                print("application/vnd.amazon.ebook")
            case "bin":
                print("application/octet-stream")
            case "gif":
                print("image/gif")
            case "jpg"|"jpeg":
                print("image/jpeg")
            case "png":
                print("image/png")
            case "pdf":
                print("application/pdf")
            case "txt":
                print("text/plain")
            case "zip":
                print("application/zip")
            case _ :
                print("it will be included in next update.")
    else :
        print("please enter extension")
main()