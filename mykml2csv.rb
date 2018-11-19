require "nokogiri"


coords = []

@doc = Nokogiri::XML(File.open("myplaces.kml"))
@doc.css('coordinates').each do |coordinates|
  coordinates.text.split(' ').each do |coordinate|
    (lat,lon,elevation) = coordinate.split(',')
    puts "#{lat},#{lon}\n"
  end
end
